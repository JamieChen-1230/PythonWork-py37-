import pika
import time
import sys

credentials = pika.PlainCredentials('jamie', '851230')
# 與RabbitMQ服務器建立連接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
# 建立rabiitmq協議的通道
channel = connection.channel()

# 在通道上聲明一個名為task_queue的隊列
channel.queue_declare(queue='task_queue', durable=True)


message = ' '.join(sys.argv[1:]) or "Hello World! %s" % time.time()
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(delivery_mode=2)  # 讓消息持久化
                      )
print(" [x] Sent %r" % message)

# 在退出程序之前，要先確保網絡緩衝區已被刷新，並且確保我們的消息有傳送到RabbitMQ，我們可以通過關閉連接來完成
connection.close()

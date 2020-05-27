import pika
import sys

credentials = pika.PlainCredentials('jamie', '851230')
# 與RabbitMQ服務器建立連接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
# 建立rabiitmq協議的通道
channel = connection.channel()
# 聲明一個exchange，類型為fanout(通常用於廣播)
channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!1"
# 不用設置routing_key了，因為我們是透過exchange來幫我們處理消息，所以不需要指定隊列
channel.basic_publish(exchange='logs', routing_key='', body=message)

print(" [x] Sent %r" % message)
connection.close()

import pika
import time


credentials = pika.PlainCredentials('jamie', '851230')
# 與RabbitMQ服務器建立連接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
# 建立rabiitmq協議的通道
channel = connection.channel()
# 在通道上聲明一個名為task_queue的隊列
channel.queue_declare(queue='task_queue', durable=True)


# 每當接收到一條消息，這個回調函數就會被調用。
def callback(ch, method, properties, body):
    print(" [x] Received %r (start)" % body)
    time.sleep(5)
    print(" [x] Done %s (end)" % body)
    print("method.delivery_tag", method.delivery_tag)
    # 除了設置auto_ack=False外，我們還顯式的發送確認消息，明確的告訴服務器消息被處理了
    ch.basic_ack(delivery_tag=method.delivery_tag)


# queue為隊列名；on_message_callback為回調函數
channel.basic_consume(on_message_callback=callback,
                      queue='task_queue',
                      auto_ack=False,  # auto_ack設為False表示不會將消息自動確認，而是要我們消費完後，才能把隊列中的此消息刪去
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
# 進入一個無窮循環，等待數據並在必要時運行回調函數。
channel.start_consuming()


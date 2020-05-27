import pika
import sys

credentials = pika.PlainCredentials('jamie', '851230')
# 與RabbitMQ服務器建立連接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
# 建立rabiitmq協議的通道
channel = connection.channel()
# 聲明一個exchange，類型為direct(通常用於組播)
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

# 不需指定隊列名字，因為RabbitMQ會自己隨機生成名字
# exclusive=True 表示排他性(不共享隊列)，因為廣播消息需要每一個消費者都要有一個隊列(且會在使用此隊列的消費者斷開後，自動將隊列刪除)
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    """
    python receive.py #  代表接收所有
    activate receive.py mysql.*  代表接收所有mysql的數據
    python receive.py mysql.error  代表只收mysql.error的數據
    """
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    # 要把剛剛隨機生成的隊列綁定到exchange(交換機)上，並且設置過濾條件，這樣生產者才知道要發送給哪個隊列
    channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=binding_key)


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(on_message_callback=callback, queue=queue_name)
print(' [*] Waiting for logs. To exit press CTRL+C')
channel.start_consuming()

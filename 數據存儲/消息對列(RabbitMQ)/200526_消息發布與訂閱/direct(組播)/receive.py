import pika
import sys

credentials = pika.PlainCredentials('jamie', '851230')
# 與RabbitMQ服務器建立連接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
# 建立rabiitmq協議的通道
channel = connection.channel()
# 聲明一個exchange，類型為direct(通常用於組播)
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# 不需指定隊列名字，因為RabbitMQ會自己隨機生成名字
# exclusive=True 表示排他性(不共享隊列)，因為廣播消息需要每一個消費者都要有一個隊列(且會在使用此隊列的消費者斷開後，自動將隊列刪除)
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    # 我們這邊設了三個級別[info] [warning] [error]，在使用命令行開啟時一定要加是哪個級別(可多選)
    # EX: python receive.py info error
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:
    # 要把剛剛隨機生成的隊列綁定到exchange(交換機)上，並且設置級別，這樣生產者才知道要發送給哪個級別的隊列
    channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(on_message_callback=callback, queue=queue_name)
print(' [*] Waiting for logs. To exit press CTRL+C')
channel.start_consuming()

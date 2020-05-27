import pika
import sys

credentials = pika.PlainCredentials('jamie', '851230')
# 與RabbitMQ服務器建立連接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
# 建立rabiitmq協議的通道
channel = connection.channel()
# 聲明一個exchange，類型為direct(通常用於組播)
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

"""
命令行輸入範例(.py後第一個參數是routing_key，第二個之後都是message)： 
python send.py mysql.info XXD
python send.py mysql.error
"""
# severity 表示級別(因為direct就是分了很多級別，然後選擇某一級別的來發送)
routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

# 這邊還是需要設置routing_key，這樣才能傳送到指定過濾的隊列
channel.basic_publish(exchange='topic_logs', routing_key=routing_key, body=message)

print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()

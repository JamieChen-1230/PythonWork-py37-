# 消息的生產者（發送者）
# 生產者傳送一條訊息到隊列中，接收者則接收隊列裡的消息。
import pika

credentials = pika.PlainCredentials('jamie', '851230')
# 與RabbitMQ服務器建立連接
# localhost表示連接到本機
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
# 建立rabiitmq協議的通道
channel = connection.channel()

# 最好接收方與傳送方都聲明一次(因為不知道sender還是receive會先啟動)
# 在通道上聲明一個名為hello的隊列
channel.queue_declare(queue='hello')

# 在RabbitMQ中，消息不會直接發送到隊列中，它需要先經過exchange
# exchange=''，exchange為空表示默認交換，它允許我們準確的指定消息該到哪個隊列
# routing_key設置隊列名稱
# body設置要傳輸的消息內容
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!123')
print(" [x] Sent 'Hello World!'")

# 在退出程序之前，要先確保網絡緩衝區已被刷新，並且確保我們的消息有傳送到RabbitMQ，我們可以通過關閉連接來完成
connection.close()

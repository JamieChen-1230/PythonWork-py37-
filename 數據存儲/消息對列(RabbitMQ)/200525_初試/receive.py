# 打印出來的消費者（接收者）
# 生產者傳送一條訊息到隊列中，接收者則接收隊列裡的消息。
import pika


# 與RabbitMQ服務器建立連接
# 連接到本地上的的代理
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 最好接收方與傳送方都聲明一次
# 聲明一個hello隊列
channel.queue_declare(queue='hello')


# 從隊列接收消息更為複雜，它要通過向隊列訂閱「回調函數」來工作。
# 每當接收到一條消息，這個回調函數就會被調用。(在這個的例子中，這個函數會在屏幕上打印消息的內容)
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


# 接下來，需要告訴RabbitMQ這個回調函數應該從我們的hello隊列接收消息
# queue為隊列名；on_message_callback為回調函數
channel.basic_consume(queue='hello', on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
# 進入一個無窮循環，等待數據並在必要時運行回調函數。
channel.start_consuming()

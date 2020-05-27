import pika
import uuid
import sys


# 這是一個斐波那契數列的客戶端類
class FibonacciRpcClient(object):
    def __init__(self):
        credentials = pika.PlainCredentials('jamie', '851230')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        # 透過RabbitMQ產生一個隊列(用於接收從server端回來的信息)
        self.callback_queue = result.method.queue
        # 定義好要從哪裡接收結果
        self.channel.basic_consume(on_message_callback=self.on_response, queue=self.callback_queue)

    # callback方法
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:  # 先判斷這個回傳結果是不是我們要的結果(用標識符去比對)
            self.response = body  # 如果是就對self.response賦值，這樣在call裡面的循環就會結束了

    def call(self, n):
        self.response = None
        # 唯一標識符，用來讓服務器端回傳結果時可以辨識是哪一個消息的結果
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',  # 一對一的發(不涉及廣播)
                                   routing_key='rpc_queue',  # 要傳消息到server端的隊列
                                   properties=pika.BasicProperties(reply_to=self.callback_queue,  # 先定義好server端回傳時所使用的隊列
                                                                   correlation_id=self.corr_id),  # 取一個唯一標識符
                                   body=str(n))

        # count = 0
        while self.response is None:
            # 用於檢測隊列中有沒有新消息，但不會阻塞
            self.connection.process_data_events()
            # count += 1
            # print('check....', count)

        return int(self.response)  # 回傳結果


fibonacci_rpc = FibonacciRpcClient()
num = sys.argv[1] if len(sys.argv) > 1 else 30
print(" [x] Requesting fib(%s)" % num)
response = fibonacci_rpc.call(num)
print(" [.] Got %r" % response)

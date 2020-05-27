import pika
import time
import random

credentials = pika.PlainCredentials('jamie', '851230')
# 與RabbitMQ服務器建立連接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
channel = connection.channel()

# 因為rpc_queue隊列只有在server端聲明，所以測試時一定要先啟動server端
channel.queue_declare(queue='rpc_queue')


# 計算斐波那契數列的方法
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def on_request(ch, method, props, body):
    n = int(body)
    print(" [.] fib(%s)" % n)
    response = fib(n)  # 計算結果
    # time.sleep(random.randint(10, 15))  # 隨機休眠5-10秒，來模擬處理任務時間

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,  # 回傳消息到client端的隊列(client端放到properties裡發過來的)
                     properties=pika.BasicProperties(
                         correlation_id=props.correlation_id),  # 同樣要把correlation_id傳回去，這樣client端才能去比對標識符
                     body=str(response))
    # 除了設置auto_ack=False外，我們還顯式的發送確認消息，明確的告訴對方消息已被處理了
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 設定接收端可同時接收的任務數量，prefetch_count=1 表示完成完一個任務後才會去取下一個任務
# 實際開發上應該要設定，因為才不會遇到其中一台機器處理速度較慢，所以堆積了很多消息還沒處理的問題發生
channel.basic_qos(prefetch_count=1)
# server端是從rpc_queue隊列中取消息
channel.basic_consume(on_message_callback=on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()

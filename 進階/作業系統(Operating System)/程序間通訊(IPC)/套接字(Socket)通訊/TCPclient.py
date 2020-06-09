"""
socket介於應用層與TCP/UDP之間，
socket會幫我們封裝TCP/UDP，所以我們不必深入了解協議就可開發。
(也可以說socket = ip(主機位置) + port(應用程序接口))
"""

from socket import *

ip_port = ('127.0.0.1', 8000)
back_log = 5
buffer_size = 1024

tcp_client = socket(AF_INET, SOCK_STREAM)  # 創建socket客戶端
tcp_client.connect(ip_port)  # 嘗試連結服務器

while True:  # 通訊循環
    msg = input('>>> ').strip()
    if not msg:
        continue
    # 信息均為字節類型
    tcp_client.send(msg.encode('utf-8'))
    data = tcp_client.recv(buffer_size)
    print('服務端發來的信息 ', data.decode('utf-8'))


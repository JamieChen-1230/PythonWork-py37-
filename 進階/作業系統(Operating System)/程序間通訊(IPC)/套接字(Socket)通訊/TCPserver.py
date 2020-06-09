"""
socket介於應用層與TCP/UDP之間，
socket會幫我們封裝TCP/UDP，所以我們不必深入了解協議就可開發。
(也可以說socket = ip(主機位置) + port(應用程序接口))
"""
from socket import *

ip_port = ('127.0.0.1', 8000)
back_log = 5
buffer_size = 1024

# AF_INET基於網路協議、SOCK_STREAM基於TCP協議
tcp_server = socket(AF_INET, SOCK_STREAM)  # 創建socket服務器
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 這行會重啟ip和端口，這樣就不會造成地址被占用的錯誤
tcp_server.bind(ip_port)  # 將地址綁到服務器
tcp_server.listen(back_log)  # 監聽鏈結，最多掛起5個連結

while True:  # 服務器循環(為了讓客戶端段開連結後還能繼續接收其他連結)
    # 阻塞在這裡，等待三次交握成功後拿到 (連結, 地址)
    conn, addr = tcp_server.accept()
    print('雙向連結為 ', conn)
    print('客戶端地址為 ', addr)

    while True:  # 通訊循環
        try:
            data = conn.recv(buffer_size)
            print('客戶端發來的信息 ', data.decode('utf-8'))
            # 信息均為字節類型
            conn.send(data.upper())
        except Exception:  # 當客戶端段開連結後會報錯，所以直接break掉，進入下一個等待連結的循環
            break


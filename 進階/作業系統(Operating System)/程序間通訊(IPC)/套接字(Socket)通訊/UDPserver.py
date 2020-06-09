"""
UDP的recvfrom本身是阻塞的，
意味著一個recvfrom(x)必須對唯一一個sendinto(y)，接收完了x個字節的數據就算完成，若是y>x數據就丟失，
這意味著UDP根本不會粘包，但是會丟數據，不可靠。
"""

from socket import *

ip_port = ('127.0.0.1', 8000)
buffer_size = 1024

# AF_INET基於網路協議、SOCK_DGRAM基於UDP協議
udp_server = socket(AF_INET, SOCK_DGRAM)  # 創建socket服務器
udp_server.bind(ip_port)  # 將地址綁到服務器
# UDP不會監聽鏈結
# TCP會  =>  tcp_server.listen(back_log)

while True:
    data, addr = udp_server.recvfrom(buffer_size)
    print('客戶端發來的信息 ', data)
    udp_server.sendto(data.upper(), addr)

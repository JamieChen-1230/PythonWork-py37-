"""
UDP的recvfrom本身是阻塞的，
意味著一個recvfrom(x)必須對唯一一個sendinto(y)，接收完了x個字節的數據就算完成，若是y>x數據就丟失，
這意味著UDP根本不會粘包，但是會丟數據，不可靠。
"""

from socket import *

ip_port = ('127.0.0.1', 8000)
buffer_size = 1024
# AF_INET基於網路協議、SOCK_DGRAM基於UDP協議
udp_client = socket(AF_INET, SOCK_DGRAM)
# UDP不用建立鏈結
# TCP要  =>  tcp_client.connect(ip_port)

while True:
    msg = input('>>> ').strip()
    if not msg:
        continue
    # 信息均為字節類型
    # UDP沒有建立鏈結，只能在sendto時決定發給誰
    udp_client.sendto(msg.encode('utf-8'), ip_port)
    data, addr = udp_client.recvfrom(buffer_size)
    print('服務端發來的信息 ', data)

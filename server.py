#encoding: utf-8
import socket, select
from queue import Queue
import threading
import os, sys

# 这个程序运行在服务器上，他可以接收到设备发的数据并将数据转发到我的电脑上

message = Queue(maxsize=1024)
socks = []

def tcp_server():
    # 创建tcp socket套接字对象 #(函数 socket.socket 创建一个 socket，该函数带有两个参数：AddressFamily, Type)
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # tcp_server = ('192.168.0.104',1883)
    # 准备目标主机的ip地址和端口号
    tcp_server = ('127.0.0.1', 1883)
    # 绑定地址
    tcp_socket.bind(tcp_server)
    # listen使套接字变为可以被动连接，即开启监听
    tcp_socket.listen()
    while True:
        # 等待客户端连接，连接后返回一个新的套接字为客户端服务，ip、port
        tcp_clientsock, tcp_clientaddr = tcp_socket.accept()
        while True:
            if message.empty() ==  False:
                get_date = message.get_nowait()  # 非阻塞，取不到值也不等
                try:
                    tcp_clientsock.send(get_date)
                    print("TCP客户端IP地址为:" + str(tcp_clientaddr) + ",数据：" + get_date.decode('utf-8'))
                except:
                    print("客户端已断开连接")
                    tcp_clientsock.close()
                    break


def udp_server():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server = ('192.168.0.104',8000)
    # udp_server = ('127.0.0.1', 8080)
    udp_socket.bind(udp_server)
    while True:
        date, udp_clientaddr= udp_socket.recvfrom(1024)
        print(date.decode('utf-8'))
        cache_data=open('mytest/myapp2/cache.txt','w')
        cache_data.write(date.decode('utf-8'))
        cache_data.close()
        # if udp_clientaddr not in socks:
        #     socks.append(udp_clientaddr)
        # if date != '':
        #     message.put_nowait(date)
        #     for s in socks:
        #         if s != udp_clientaddr:
        #             udp_socket.sendto(date, s)
        #             print(s)


if __name__ == "__main__":
    # tcp = threading.Thread(target=tcp_server)
    udp = threading.Thread(target=udp_server)
    # tcp.start()
    udp.start()

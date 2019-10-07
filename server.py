import socket, select
from queue import Queue
import threading
import os, sys

# ������������ڷ������ϣ������Խ��յ��豸�������ݲ�������ת�����ҵĵ�����

message = Queue(maxsize=1024)
socks = []

def tcp_server():
    # ����tcp socket�׽��ֶ��� #(���� socket.socket ����һ�� socket���ú�����������������AddressFamily, Type)
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # tcp_server = ('192.168.0.104',1883)
    # ׼��Ŀ��������ip��ַ�Ͷ˿ں�
    tcp_server = ('127.0.0.1', 1883)
    # �󶨵�ַ
    tcp_socket.bind(tcp_server)
    # listenʹ�׽��ֱ�Ϊ���Ա������ӣ�����������
    tcp_socket.listen()
    while True:
        # �ȴ��ͻ������ӣ����Ӻ󷵻�һ���µ��׽���Ϊ�ͻ��˷���ip��port
        tcp_clientsock, tcp_clientaddr = tcp_socket.accept()
        while True:
            if message.empty() ==  False:
                get_date = message.get_nowait()  # ��������ȡ����ֵҲ����
                try:
                    tcp_clientsock.send(get_date)
                    print("TCP�ͻ���IP��ַΪ:" + str(tcp_clientaddr) + ",���ݣ�" + get_date.decode('utf-8'))
                except:
                    print("�ͻ����ѶϿ�����")
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

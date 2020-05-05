# 3. 编写一个UDP的聊天程序
# 每个程序可以同时进行消息的发送和接收
import socket
from threading import Thread


# 循环从键盘读入消息并发送
# :param addr 接收方的ip地址和端口号
def send(addr):
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        msg = input()  # 从键盘读入消息
        udp.sendto(msg.encode('utf-8'), addr)


# 持续监听指定端口收到的消息
# 将收到的消息打印出来
# :param addr 监听的ip和端口号
def recv(addr):
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind(addr)
    while True:
        # 收不到消息该方法将阻塞
        recv_data, recv_addr = udp.recvfrom(1024)

        print('from <{}:{}>:'.format(recv_addr[0], recv_addr[1]))
        print(recv_data.decode('utf-8').rstrip())


if __name__ == '__main__':
    ip, port = input('请输入接收方的ip和端口号: ').split()
    dst_addr = (ip, int(port))

    port = int(input('请输入监听的端口号: '))
    src_addr = ('', port)

    # 发送线程
    Thread(target=send, args=(dst_addr, )).start()
    # 接收线程
    Thread(target=recv, args=(src_addr, )).start()

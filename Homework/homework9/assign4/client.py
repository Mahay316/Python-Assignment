# 4. 设计一款能实现多人聊天的系统
# 使用socket和多线程技术，编写多人聊天室

# 客户端程序，与服务器建立TCP连接
import os
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


# 接收键盘输入，将消息发送给服务器
def send(username, sock):
    while True:
        msg = input()
        # 输入/quit退出程序
        if msg == '/quit':
            sock.close()
            break
        # 格式化消息
        msg = f'{username} say: {msg}'
        sock.send(msg.encode('utf-8'))

    print('程序关闭')
    os._exit(0)  # 正常结束程序


# 循环接收来自服务器的消息
def recv(sock):
    while True:
        try:
            msg = sock.recv(1024)
        except ConnectionResetError:
            print('连接断开')
            # 若连接已被对方关闭，产生ConnectionResetError
            sock.close()
            break
        except OSError:
            # 若本地socket已被关闭，产生OSError
            break
        else:
            print(msg.decode('utf-8'))

    print('程序关闭')
    os._exit(0)  # 正常退出程序


if __name__ == '__main__':
    username = input('请输入你的用户名: ')

    # 连接服务器
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    try:
        tcp_socket.connect(('192.168.2.104', 8888))
    except IOError:
        print('无法连接到服务器')
        os._exit(1)  # 异常退出程序

    print('成功连接到服务器')
    print('在命令行输入信息聊天')
    print('输入命令/quit退出')
    Thread(target=send, args=(username, tcp_socket)).start()
    Thread(target=recv, args=(tcp_socket, )).start()

# 4. 设计一款能实现多人聊天的系统
# 使用socket和多线程技术，编写多人聊天室

# 服务器端程序，接受客户端连接，并把收到的消息转发给所有客户端
import os
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


class Server:
    # :param port 服务器程序监听的端口
    def __init__(self, port):
        self.port = port
        self.addr = ('', port)
        # 用户列表，保存为socket: addr键值对
        self.users = {}

    def start(self):
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind(self.addr)
        # 开始监听连接请求
        self.server_socket.listen(5)

        # 另开一个线程接受连接，主线程接受控制命令
        Thread(target=self.accept_conn).start()

    def accept_conn(self):
        while True:
            client, addr = self.server_socket.accept()
            self.users[client] = addr
            print('<{}:{}>连接'.format(addr[0], addr[1]))

            # 开启一个新线程负责与该客户端进行通信
            Thread(target=self.recv_msg, args=(client, )).start()

    # 接受sock发来的消息，并转发给所有其他用户
    def recv_msg(self, sock):
        addr = self.users[sock]
        while True:
            try:
                msg = sock.recv(1024)
                print('<{}:{}>:'.format(addr[0], addr[1]), msg.decode('utf-8'))

                # 转发
                for s in self.users.keys():
                    if s != sock:
                        s.send(msg)
            except ConnectionResetError:
                print('<{}:{}>下线'.format(addr[0], addr[1]))
                # 客户端断开连接
                sock.close()
                del self.users[sock]
                break
            except OSError:
                # 服务器程序关闭
                break

    def close(self):
        # 释放连接
        self.server_socket.close()
        for s in self.users.keys():
            s.close()
        os._exit(0)


if __name__ == '__main__':
    s = Server(8888)
    s.start()
    print('服务器开启')
    print('输入命令/quit关闭服务')

    while True:
        cmd = input()
        if cmd == '/quit':
            s.close()
        else:
            print('无效命令')

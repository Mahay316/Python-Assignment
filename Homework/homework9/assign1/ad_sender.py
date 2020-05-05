# 测试使用udp socket循环发送数据
# 使用网络调试工具接收
import socket


def main():
    # 创建UDP套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 发送目标地址
    dst_addr = ('192.168.2.104', 8888)

    while True:
        data = input('输入发送的数据（/quit退出）: ')
        if data == '/quit':
            break

        udp_socket.sendto(data.encode('utf-8'), dst_addr)


if __name__ == '__main__':
    main()

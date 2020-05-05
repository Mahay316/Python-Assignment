# 测试使用udp socket发送数据
# 使用网络调试工具接收
import socket


def main():
    # 1. 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2. 准备接收方的地址
    # '192.168.1.24'表示目的ip地址
    # 8888表示目的端口
    dest_addr = ('192.168.2.104', 8888)  # 注意是元组，ip是字符串，端口是数字

    # 3. 从键盘获取数据
    send_data = input("请输入要发送的数据: ")
    # 4. 发送数据到指定的电脑上的指定程序中
    # udp发送数据前不需要建立连接
    udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

    # 5 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()

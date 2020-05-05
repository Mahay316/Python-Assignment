# 测试使用udp socket在指定端口持续监听，接收数据
# 使用网络调试工具发送
import socket


def main():
    # 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    local_addr = ('', 9999)
    # 监听指定端口
    udp_socket.bind(local_addr)

    while True:
        recv_data, recv_addr = udp_socket.recvfrom(1024)  # 最多接收1024字节
        print('from <{}:{}>:'.format(recv_addr[0], recv_addr[1]))
        print(recv_data.decode('utf-8').rstrip())


if __name__ == '__main__':
    main()

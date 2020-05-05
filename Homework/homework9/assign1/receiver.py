# 测试使用udp socket在指定端口监听，接收数据
# 使用网络调试工具发送
import socket


def main():
    # 绑定端口信息
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # localhost:9999
    local_addr = ('', 9999)
    udp_socket.bind(local_addr)

    # 接收数据
    # 1024表示本次接收的最大字节数
    recv_data, recv_addr = udp_socket.recvfrom(1024)
    print('from <{}:{}>:'.format(recv_addr[0], recv_addr[1]))
    print(recv_data.decode('utf-8'))

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()

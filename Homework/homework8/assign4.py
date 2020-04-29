# 4. 多进程通讯
# 编写一个简单的聊天程序
# 其中一个进程发送文字聊天消息（从键盘输入文字消息）
# 另外一个进程接收并打印消息
from multiprocessing import Process, Queue


# 循环从键盘读入文字，写入共享队列中
# 当输入terminator指定的字符串时退出
def sender(q, terminator='/bye'):
    while True:
        msg = input()
        q.put(msg)
        if msg == terminator:
            break


def receiver(q, terminator='/bye'):
    while True:
        # 从队列取出消息，没消息时阻塞
        msg = q.get()
        if msg == terminator:
            break
        print('收到消息:', msg)


if __name__ == '__main__':
    queue = Queue()  # 消息队列
    p = Process(target=receiver, args=(queue, ))
    p.start()
    sender(queue)

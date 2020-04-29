# 1. 有100个同学的分数，数据请用随机函数生成
#   A 利用多线程程序（比如，5个线程）快速输出这100个同学的信息
#   B 利用线程池来实现
from time import sleep
from random import randint
from threading import Thread, current_thread
from concurrent.futures import ThreadPoolExecutor


# 多线程执行的函数
# 打印成绩列表score_list中从start开始的length个元素
def print_score(score_list, start, length):
    for i in range(start, start + length):
        print(score_list[i], end=' ')


length = 100
scores = [randint(0, 100) for _ in range(length)]
len_per_thread = int(length / 5)
# A 使用多线程的版本
# 将任务分配给五个进程
print('----- Threads -----')
for i in range(4):
    kwargs = {
        'score_list': scores,
        'start': len_per_thread * i,
        'length': len_per_thread
    }
    t = Thread(target=print_score, kwargs=kwargs)
    t.start()
# 处理列表长度无法被整除的情况
kwargs = {
    'score_list': scores,
    'start': len_per_thread * 4,
    'length': length - len_per_thread * 4
}
t = Thread(target=print_score, kwargs=kwargs)
t.start()

sleep(1)
print('\n----- Thread Pool -----')
# B 使用线程池的版本
with ThreadPoolExecutor(max_workers=5) as executor:
    for i in range(4):
        executor.submit(print_score, scores,
                        len_per_thread * i, len_per_thread)
    executor.submit(print_score, scores,
                    len_per_thread * 4, length - len_per_thread * 4)

# 3. 多进程练习：
# (100000并不能体现出多进程的速度，因此我改成了1000000)
# 计算1~1000000之间所有素数的个数，要求如下
# - 编写函数判断一个数字是否为素数，然后统计素数的个数
# - 对比1: 对比使用多进程和不使用多进程两种方法的统计速度
# - 对比2：对比开启4个多进程和开启10个多进程两种方法的速度
import os
from math import sqrt
from time import perf_counter  # 高精度计时
from multiprocessing import Process, Manager


# 判断num是否是素数
# 是素数返回True，否则返回False
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


# 统计[start, end)间的整数中素数的数量
# 将结果存放在字典dict_res中
def count_prime(start, end, dict_res):
    count = 0
    for i in range(start, end):
        if is_prime(i):
            count += 1

    dict_res[os.getpid()] = count


if __name__ == '__main__':
    # ------- 对比1 -------- #
    print('对比1: 单进程 vs 8进程')
    t1 = perf_counter()

    dict_res = {}
    count_prime(1, 1000001, dict_res)
    print('单进程结果:', sum(dict_res.values()), flush=True)

    t2 = perf_counter()

    dict_res = Manager().dict()
    tasks = []
    for i in range(8):
        p = Process(target=count_prime,
                    args=(1 + 125000 * i, 1 + 125000 * (i + 1), dict_res))
        tasks.append(p)
        p.start()
    # 父进程等待全部子进程执行完成
    for p in tasks:
        p.join()
    print('8进程结果:', sum(dict_res.values()))

    t3 = perf_counter()
    print('单进程: %.6fs' % (t2 - t1))  # ~11.36s
    print('8进程: %.6fs' % (t3 - t2))  # ~2.56s

    # -------- 对比2 -------- #
    print('\n对比2: 4进程 vs 10进程')
    t1 = perf_counter()

    dict_res = Manager().dict()
    tasks = []
    for i in range(4):
        p = Process(target=count_prime,
                    args=(1 + 250000 * i, 1 + 250000 * (i + 1), dict_res))
        tasks.append(p)
        p.start()
    # 父进程等待全部子进程执行完成
    for p in tasks:
        p.join()
    print('4进程结果:', sum(dict_res.values()))

    t2 = perf_counter()

    dict_res = Manager().dict()
    tasks = []
    for i in range(10):
        p = Process(target=count_prime,
                    args=(1 + 100000 * i, 1 + 100000 * (i + 1), dict_res))
        tasks.append(p)
        p.start()
    # 父进程等待全部子进程执行完成
    for p in tasks:
        p.join()
    print('10进程结果:', sum(dict_res.values()))

    t3 = perf_counter()
    print('4进程: %.6fs' % (t2 - t1))  # ~4.39s
    print('10进程: %.6fs' % (t3 - t2))  # ~2.37s

# 1. 编写一个装饰器，能计算其他函数的运行时间

from time import perf_counter_ns


# 计算函数运行时间的装饰器
# 该装饰器只适用于没有返回值的函数
def time_counter(func):
    def wrapper(*args, **kwargs):
        start = perf_counter_ns()
        func(*args, **kwargs)
        end = perf_counter_ns()
        print("函数{0}运行了{1}ns".format(func.__name__, end - start))

    return wrapper


# 测试函数
@time_counter
def test():
    i = 0
    while i < 100000:
        i += 1


test()

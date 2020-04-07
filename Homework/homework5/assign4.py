# 4. 编写装饰器来实现，对目标函数进行装饰，分3种情况：
# 目标函数无参数无返回值，目标函数有返回值，目标函数有参数有返回值
#
# 三个目标函数分别为：
# A. 打印输出20000之内的素数
# B. 计算整数2 - 10000之间的素数的个数
# C. 计算整数2 - M之间的素数的个数
from math import sqrt


# 无参数无返回值函数的装饰器
def common_dec(func):
    def wrapper():
        print('进入无参数无返回值函数的装饰器')
        func()
        print('退出无参数无返回值函数的装饰器')

    return wrapper


# 无参数有返回值函数的装饰器
def ret_dec(func):
    def wrapper():
        print('进入有参数无返回值函数的装饰器')
        ret = func()
        print('退出有参数无返回值函数的装饰器')
        return ret

    return wrapper


# 有参数有返回值函数的装饰器
def arg_dec(func):
    def wrapper(*args, **kwargs):
        print('进入有参数有返回值函数的装饰器')
        ret = func(*args, **kwargs)
        print('退出有参数有返回值函数的装饰器')
        return ret

    return wrapper


# 打印输出20000之内的素数
@common_dec
def common_prime():
    for i in range(2, 20000):
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            print(i, end=' ')
    print()


# 计算整数2 - 10000之间的素数的个数
@ret_dec
def ret_prime():
    count = 0
    for i in range(2, 10000):
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            count += 1

    return count


# 计算整数2 - M之间的素数的个数
@arg_dec
def arg_prime(n):
    count = 0
    for i in range(2, n):
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            count += 1

    return count


common_prime()
print("2 - 10000之间有{0}个素数".format(ret_prime()))
print("2 - {0}之间有{1}个素数".format(5000, arg_prime(5000)))

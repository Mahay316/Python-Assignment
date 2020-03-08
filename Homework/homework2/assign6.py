# 6. 定义一个函数, 打印输出n以内的斐波那契数列


def fib(n):
    "打印n以内的斐波那契数列"
    a, b = 0, 1
    while b <= n:
        print(b, end=' ')
        # 递推法求斐波那契数列
        a, b = b, a + b
    print()


fib(100)
fib(10000)

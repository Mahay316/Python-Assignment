# 3. 编写一个函数, 传入一个数字列表, 输出列表中的奇数
# 数字列表请用随机数函数生成

from random import randint


def print_odd(num_list):
    "打印传入列表中的所有奇数"
    for i in num_list:
        if i % 2 == 1:
            print(i, end=' ')


# 使用列表解析式生成测试列表
test_list = [randint(0, 100) for _ in range(20)]
print_odd(test_list)

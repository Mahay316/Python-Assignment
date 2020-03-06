# 练习使用匿名函数和列表解析式
num = [x for x in range(1, 21)]
num = filter(lambda x: x % 2 == 0, num)
print("0-20之间的偶数", list(num))

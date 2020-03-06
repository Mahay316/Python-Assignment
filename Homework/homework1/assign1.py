# 1. 元素输出和查找
# 请输出0-50之间的奇数，偶数，质数
# 能同时被2和3整除的数

from math import sqrt

# 练习使用列表解析式生成列表
odd = [x for x in range(51) if x % 2 == 1]
print("奇数:")
print(odd)
even = [x for x in range(51) if x % 2 == 0]
print("偶数:")
print(even)

# 练习使用循环判断质数
print("质数:")
for i in range(2, 51):
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        print(i, end=' ')
print()

# 练习使用列表解析式生成列表
arr = [x for x in range(51) if x % 2 == 0 if x % 3 == 0]
print("能被2和3整除的数:")
print(arr)

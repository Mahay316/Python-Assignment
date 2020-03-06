# 5. 使用random模块，生成随机数，来初始化一个列表，元组
# 使用random模块的randint()函数来生成随机数

from random import randint

# 利用列表解析式配合randint()函数生成随机列表
rand_list = [randint(-10, 10) for _ in range(10)]
print(rand_list)

# (randint(-10, 10) for _ in range(10)) 的类型是生成器
# 使用tuple()类型转换成元组
rand_tuple = tuple((randint(-10, 10) for _ in range(10)))
print(rand_tuple)

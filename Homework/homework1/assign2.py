# 2. 一个字典中，存放了10个学生的学号(key)和分数(value)
# 请筛选输出，大于80分的同学（按照格式：学号：分数）

from random import randint

# 生成随机测试数据
# 元素格式样例： '007': 89
score = {'%03d' % randint(1, 30): randint(0, 100) for _ in range(10)}
print(score)

# 输出成绩大于80分的学生信息
print("学号  分数")
print("----------")
for k, v in score.items():
    if (v > 80):
        print("%s: %3d" % (k, v))

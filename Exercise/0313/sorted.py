# 练习使用sorted()函数排序复杂数据
from random import randint


def printScore(score):
    print("    姓名   成绩")
    print("----------------")
    for n, s in score:
        print("%10s %3d" % (n, s))


scores = [("Student" + str(i), randint(0, 100)) for i in range(10)]
# 使用lambda表达式指定排序的key
scores_sorted = sorted(scores, key=lambda k: k[1])
print("原成绩:")
printScore(scores)
print("升序排列后的成绩:")
printScore(scores_sorted)

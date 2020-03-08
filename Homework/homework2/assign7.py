# 7. 随机生成20个学生的成绩，判断这20个学生成绩的等级
# A -> 成绩 >= 90
# B -> 成绩在 [80, 90)
# C -> 成绩在 [70, 80)
# D -> 成绩 < 70

from random import randint


# 返回一个与成绩对应的等级列表
def classify(scores):
    "判断成绩列表中每个成绩对应的等级"
    res = []
    for s in scores:
        if s >= 90:
            res.append('A')
        elif s >= 80:
            res.append('B')
        elif s >= 70:
            res.append('C')
        else:
            res.append('D')

    return res


scores = [randint(0, 100) for _ in range(30)]
for s, c in zip(scores, classify(scores)):
    print("成绩: %3d -> 等级: %s" % (s, c))

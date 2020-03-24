# 3. 读取文件中保存的10个学生成绩名单信息
# (学号, 姓名, Python课程分数)
# 然后按照分数从高到低进行排序输出
import os

score_file = 'score.txt'

os.chdir('Homework/homework3')
scores = []
try:
    with open(score_file, 'r', encoding='utf-8') as f:
        for line in f:
            scores.append(line)
except FileNotFoundError:
    print("找不到文件{0}，请检查文件名和路径的正确性".format(score_file))
except IOError:
    print("无法打开文件{0}".format(score_file))
else:
    scores = list(map(lambda x: x.split(), scores))
    # 将成绩转换成int类型
    try:
        for i in range(len(scores)):
            scores[i][2] = int(scores[i][2])
    except ValueError:
        print("数据文件格式错误，程序终止")
        raise
    scores.sort(key=lambda x: x[2], reverse=True)

    print(" 学号  姓名   成绩 ")
    print("-" * 20)
    for no, na, s in scores:
        print("%3s   %-8s %3d" % (no, na, s))

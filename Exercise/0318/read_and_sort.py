# 练习4 读取score.txt文件中的内容
# 对分数进行降序排序后
# 打印并输出到另一个文件sorted.txt中
import os

os.chdir('Exercise/0318')

score_list = []
with open('score.txt', 'r', encoding='utf-8') as src:
    title = src.readline()  # 读取标题
    res = src.readline()
    while len(res) > 0:
        score_list.append(res)
        res = src.readline()

with open('sorted.txt', 'w', encoding='utf-8') as dst:
    score_list.sort(key=lambda x: x.split()[2])

    # 打印标题
    print(title, end='')
    dst.write(title)
    # 打印成绩
    for item in score_list:
        print(item, end='')
    dst.writelines(score_list)

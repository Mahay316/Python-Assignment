# 2. 从input.txt中读取之前输入的数据，存入列表中
# 再加上行号打印显示，格式如下:
#   1.#第一行： xxxx
#   2.#第二行： xxxx
import os

buf = []
os.chdir('Homework/homework3')
output_f = 'input.txt'  # 输入文件
try:
    with open(output_f, 'r', encoding='utf-8') as f:
        for line in f:
            buf.append(line)
except FileNotFoundError:
    print("找不到文件{0}，请检查文件名和路径的正确性".format(output_f))
except IOError:
    print("无法打开文件{0}".format(output_f))
else:
    for i in range(len(buf)):
        print("%3d %s" % (i + 1, buf[i]), end='')

# 1. 读取键盘输入的任意行文字信息，当输入空行时结束输入
# 将读入的字符串存于列表
# 然后将列表里面的内容写入到文件input.txt中
import os

buf = []  # 保存输入的列表
text = input("输入任意行文字保存入文件，输入空行结束程序:\n")
while len(text) > 0:
    buf.append(text)
    text = input()

os.chdir('Homework/homework3')  # 切换工作路径
output_f = 'input.txt'  # 输出文件
try:
    with open(output_f, 'w', encoding='utf-8') as f:
        # 给每一行加上换行符
        buf = map(lambda x: x + '\n', buf)
        f.writelines(buf)
except IOError as e:
    print("发生IOError异常", e)
    print("无法打开文件{0}".format(output_f))

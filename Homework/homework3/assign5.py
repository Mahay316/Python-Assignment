# 5. 完成以下文件综合编程迷你项目
# (1) 创建一个文件Blowing in the wind.txt
# (2) 在文件头部插入歌名“Blowin' in the wind”
# (3) 在歌名后插入歌手名“Bob Dylan”
# (4) 在文件末尾加上字符串“1962 by Warner Bros.Inc.”
# (5) 在屏幕上打印文件内容
import os

os.chdir('Homework/homework3')
filename = 'Blowing in the wind.txt'
buf = []
# 读入文件内容
try:
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            buf.append(line)
except FileNotFoundError:
    print("找不到文件{0}，请检查文件名和路径的正确性".format(filename))
except IOError:
    print("无法打开文件{0}".format(filename))

buf.insert(0, "Blowin' in the wind\n")
buf.insert(1, "---- Bob Dylan\n")
buf.append("\n")  # 插入空行，使格式美观
buf.append("1962 by Warner Bros.Inc.\n")

# 写回修改到文件
try:
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(buf)
except IOError:
    print("无法打开文件{0}".format(output_f))

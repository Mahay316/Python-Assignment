# 练习2 练习打开上一级目录其他子目录中的文件
import os

# 将工作路径切换至当前文件夹
# 以便使用相对路径访问其他文件
os.chdir('Exercise/0318/b')
with open('../a/test.txt', encoding='utf-8') as file:
    print(file.read())

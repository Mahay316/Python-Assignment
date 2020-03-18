# 练习2 打开同级文件和子目录中的文件
import os

# 将工作路径切换至当前文件夹
# 以便使用相对路径访问其他文件
os.chdir('Exercise/0318')

# 同级文件
# Windows平台默认编码为GBK
# 但vscode创建的文本文件编码为UTF-8
# 强制使用UTF-8打开文件
with open('os_path_test.py', encoding='utf-8') as file:
    print(file.read())

# 子目录中文件
with open('a/test.txt', encoding='utf-8') as file:
    print(file.read())

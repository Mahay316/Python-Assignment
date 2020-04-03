# 6. 通过Python来实现显示给定文件夹下的所有文件和文件夹
# 如果是文件，显示大小
# 输出格式效果如下:
# 名称    日期     类型(文件夹或文件)    大小

import os
from time import ctime


# 程序循环接受用户输入
# 接受输入前打印提示符，显示当前所在目录
# 输入 ll 打印当前目录内容
# 输入 ll 相对路径 打印当前目录中的指定子目录内容
# 输入 ll 绝对路径 打印指定目录内容
# 输入 cd 路径 切换当前目录
# 输入 quit 退出程序
def print_dir(dir_path):
    content = os.listdir(dir_path)
    files = []
    print("    名称", " " * 28, "修改日期", end="")
    print(" " * 14, "类型", " " * 6, "大小")
    for c in content:
        abs_c = os.path.join(dir_path, c)
        if os.path.isfile(abs_c):
            files.append(c)  # 暂时保存文件，后于文件夹输出
        else:
            print("%-30s%-30s" % (c, ctime(os.path.getmtime(abs_c))), end="")
            print("文件夹")
    # 文件夹输出完成，开始输出文件
    for c in files:
        abs_c = os.path.join(dir_path, c)
        print("%-30s%-30s" % (c, ctime(os.path.getmtime(abs_c))), end="")
        print("文  件%10sB" % os.path.getsize(abs_c))


# 对命令进行解析并执行
def parse(cmd):
    if cmd is None or cmd == '':
        return

    cmd = cmd.strip().split()
    if cmd[0] == 'll' or cmd[0] == 'ls':
        if len(cmd) == 2:
            print_dir(cmd[1])
        else:
            print_dir(".")
    elif cmd[0] == 'cd':
        if len(cmd) != 2:
            print("command syntax error")
        else:
            try:
                os.chdir(cmd[1])
            except FileNotFoundError:
                print("directory not found")
    else:
        print("unknown command")


while True:
    cmd = input("{}$> ".format(os.getcwd()))
    if "quit" == cmd:
        break
    else:
        parse(cmd)

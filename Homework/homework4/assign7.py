# 7. 使用python代码统计一个文件夹中所有文件的总大小

import os


# 返回指定文件夹中所有文件总大小
def total_size(dir_path):
    sum = 0
    content = os.listdir(dir_path)
    for c in content:
        abs_c = os.path.join(dir_path, c)
        if os.path.isfile(abs_c):
            sum += os.path.getsize(abs_c)

    return sum


# 将文件大小（字节）转化到合适的单位
# 并以字符串的形式返回
def convert_size(size):
    if size < 1024:
        res = str(size) + "B"
    elif size < 1024 * 1024:
        res = str(size // 1024) + "M"
    else:
        res = str(size // (1024 * 1024)) + "G"

    return res


print(convert_size(total_size("Homework/homework4")))

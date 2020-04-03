# 5. 通过Python来模拟实现一个txt文件的拷贝过程

import os


# 该文件src拷贝到dst
# dst可以和src不同名
def copy(src, dst):
    if not os.path.exists(src) or not os.path.isfile(src):
        print(f"文件{src}不存在，无法拷贝")
        return

    # 不关注文件类型，均以二进制对待
    with open(src, 'rb') as f1, open(dst, 'wb') as f2:
        for line in f1:
            f2.write(line)


os.chdir('Homework/homework4')
copy('src.txt', 'dst.txt')

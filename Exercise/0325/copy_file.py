# 练习：将一个文件夹下的文件复制到另一个文件夹中
import os


# 该函数将覆盖dst目录下的已有同名文件
def copy(src, dst):
    fileList = os.listdir(src)
    for f in fileList:
        sf = os.path.join(src, f)
        df = os.path.join(dst, f)
        if os.path.isfile(sf):
            with open(sf, 'rb') as f1, open(df, 'wb') as f2:
                for line in f1:
                    f2.write(line)


os.chdir('Exercise/0325')
copy('src', 'dst')

# 4. 在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
# 将当前img目录所有以.png结尾的后缀名改为.jpg
from os import chdir, listdir, rename
# import string
# from random import randint

chdir('Homework/homework3/img')
# # 生成随机文件名
# suffix = ['.png', '.txt', '.jpg']
# # digits and letters
# dal = string.ascii_letters + string.digits
# # 生成10个文件
# for i in range(10):
#     # 随机生成长度为3-10的文件名
#     filename = ''.join([dal[randint(0, len(dal) - 1)] for _ in range(randint(3, 10))])
#     # 随机选择文件后缀
#     filename += suffix[randint(0, len(suffix) - 1)]
#     with open(filename, 'w'):
#         pass

files = listdir('.')
for f in files:
    if f.endswith('.png'):
        rename(f, f.strip('.png') + '.jpg')

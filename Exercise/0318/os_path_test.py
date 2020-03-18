# 练习1 使用os.path模块下函数的使用
import os

# 打印文件名
print(os.path.basename(r'D:\Python\water.py'))
# 打印路径名
print(os.path.dirname(r'D:\Python\water.py'))
# 分隔路径名和文件名
print(os.path.split(r'D:\Python\water.py'))
# 拼接路径
print(os.path.join(r'D:\Python', 'water.py'))

# 练习5 使用pickle模块序列化对象
# 给定一个字典，保存了5个同学的学号、姓名、年龄
# 使用pickle模块将数据对象保存到文件中去

import os
import pickle

infos = [
    {'no': '1201', 'name': '张三', 'age': 18},
    {'no': '1203', 'name': '李四', 'age': 20},
    {'no': '1205', 'name': '李明', 'age': 19},
    {'no': '1206', 'name': '小红', 'age': 19},
    {'no': '1208', 'name': '小刚', 'age': 23}
]

os.chdir('Exercise/0318')
# 序列化
with open('infos', 'wb') as f:
    pickle.dump(infos, f)

# 反序列化
with open('infos', 'rb') as f:
    load_infos = pickle.load(f)
    print(load_infos)

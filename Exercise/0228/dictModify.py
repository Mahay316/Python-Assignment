# 定义字典，并对字典进行增删改操作
Mahay = {
    'no': '12018111011',
    'name': '赵鹏飞',
    'class': '软件1801',
    'age': 19
}

Mahay['school'] = 'NCEPU'  # 添加元素
Mahay['age'] = 20  # 修改元素
del Mahay['no']  # 删除键值对
print(Mahay)

# 8. 设计一个数据结构，用来存放10个员工的信息并初始化
# 每个员工信息包括：工号，姓名，工龄，工资
# 将这10个员工，按照工资从高到低打印输出；
# 提示：可以组合使用我们的序列数据类型

# 用字典存储一个员工的信息
# 如：{'no': '012', 'name': 'Tom', 'work_age': 10, 'salary': 5000}
# 用列表保存所有员工的信息

infos = [
    {'no': '001', 'name': 'Albert', 'work_age': 5, 'salary': 3000},
    {'no': '002', 'name': 'Bob', 'work_age': 8, 'salary': 5000},
    {'no': '005', 'name': 'Catherine', 'work_age': 5, 'salary': 3500},
    {'no': '006', 'name': 'David', 'work_age': 7, 'salary': 10000},
    {'no': '007', 'name': 'Eric', 'work_age': 7, 'salary': 8500},
    {'no': '008', 'name': 'Frank', 'work_age': 2, 'salary': 3000},
    {'no': '010', 'name': 'Green', 'work_age': 6, 'salary': 5500},
    {'no': '011', 'name': 'Hobby', 'work_age': 5, 'salary': 4500},
    {'no': '016', 'name': 'Isaac', 'work_age': 1, 'salary': 2900},
    {'no': '017', 'name': 'Jack', 'work_age': 9, 'salary': 7500}
]

# 选择排序
for i in range(len(infos)):
    max = i
    for j in range(i + 1, len(infos)):
        if infos[max]['salary'] < infos[j]['salary']:
            max = j
    tmp = infos[i]
    infos[i] = infos[max]
    infos[max] = tmp

# 按顺序输出
for i in infos:
    print(f"工号: {i['no']}, 姓名: {i['name']}", end='')
    print(f", 工龄: {i['work_age']}, 工资: {i['salary']}")

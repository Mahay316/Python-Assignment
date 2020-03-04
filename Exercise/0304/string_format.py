# 测试多种拼接、格式化字符串的方式
# test code snippet #1
username = input('username: ')
password = input('password: ')
print(username, password)

# test code snippet #2.1
name = input("name: ")
age = input("age: ")
skill = input("skill: ")
salary = input("salary:")
info = ' --- info of ' + name + ' name: ' + name + ' age: ' + age + ' skill: ' + skill + ' salary: ' + salary + ' '
print(info)

# test code snippet #2.2
name = input("name: ")
age = input("age: ")
skill = input("skill: ") 
salary = input("salary: ")
info1 = ' --- info of %s --- Name:%s Age:%s Skill:%s Salary:%s ' % (name, name, age, skill, salary)
print(info1)

# test code snippet #3
name = input("username：")
age = input("age：")
skill = input("skill：")
salary = input("salary：")
# 此处是赋值
info = ' --- info of {_name} Name：{_name} Age：{_age} Skill：{_skill} Salary：{_salary} '.format(_name=name, _age=age, _skill=skill, _salary=salary)
print(info)

# test code snippet #4
name = input("name：")
age = input("age：")
skill = input("skill：")
salary = input("salary：")
info = ' --- info of {0}--- Name：{0} Age：{1} Skill：{2} Salary：{3} '.format(name, age, skill, salary)
print(info)
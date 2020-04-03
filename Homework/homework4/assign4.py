# 4. 模拟用户登录:
# 5个同学的姓名、账号和密码（加密后的），保存在一个文件上
# 系统提示：请输入登录同学姓名
# 正确后，请输入账号
# 正确后，提示请输入密码（输入明文）
# 如果都正确，打印提示，您登录成功，否则提示失败

from hashlib import md5
from os import chdir

# 切换到密码文件所在位置
chdir('Homework/homework4')
pw = []
# 读取密码记录
with open('passwd', 'r', encoding='utf-8') as f:
    for line in f:
        pw.append(line.split())

name = input("请输入姓名: ")
# 筛出所有姓名符合的记录，假定姓名可能重复，但账号唯一
pw = list(filter(lambda x: x[0] == name, pw))

if len(pw):  # 姓名符合的记录长度不为0
    account = input("姓名存在，请输入账号: ")
    pw = list(filter(lambda x: x[1] == account, pw))
    if len(pw):  # 账号符合的记录长度不为0
        passwd = input("账号正确，请输入密码: ")
        # 由于账号唯一，pw这时仅可能有一条记录
        if pw[0][2] == md5(bytes(passwd, encoding='utf-8')).hexdigest():
            print("欢迎你,", name)
        else:
            print("密码错误，请检查输入")
    else:
        print("账号错误，请检查输入")
else:
    print("姓名不存在，请检查输入")

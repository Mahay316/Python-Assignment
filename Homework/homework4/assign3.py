# 3. 从键盘输入5个同学的账号和密码
# 将他们的姓名、账号和密码（密码需要加密）保存到一个文件中
# Tom    admin   XXXXX
# Jack   root    XXXXX

from hashlib import md5
from os import chdir

chdir('Homework/homework4')
with open('passwd', 'w', encoding='utf-8') as f:
    print("请输入5位同学的账号信息，格式为: 姓名 账号 密码")
    for i in range(5):
        # 姓名 账号 密码
        infos = input(f"{i + 1}: ").split()
        f.write(infos[0] + ' ')
        f.write(infos[1] + ' ')
        # string对象需编码成bytes对象，且仅能接受ASCII字符
        f.write(md5(bytes(infos[2], encoding='utf-8')).hexdigest())
        f.write('\n')

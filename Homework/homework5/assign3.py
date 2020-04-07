# 3. 编写一个装饰器，为多个函数加上认证的功能
# 必须输入用户的账号密码，才能调用这个函数
auth = False   # 登录状态


# 验证用户身份信息
# 验证成功返回True并保持登录状态，否则返回False
def authenticate():
    global auth
    usr = input('请输入用户名: ')
    passwd = input('请输入密码: ')
    if usr == 'admin' and passwd == 'admin':
        auth = True
        return True

    return False


def auth_dec(func):
    def wrapper(*args, **kwargs):
        if auth or authenticate():
            return func(*args, **kwargs)
        print('函数调用权限不足')
        print('对于函数{0}的访问被拒绝'.format(func.__name__))

    return wrapper


# 测试函数
@auth_dec
def print_log():
    print("admin's log here")


# 测试函数
@auth_dec
def add_user(name):
    print("user added: {0}".format(name))


print_log()
add_user('John')
add_user('Peter')

# 练习：装饰器的使用
def log(func):
    def wrapper(*args):
        res = func(*args)
        # 记录日志
        print("add function invoked")
        return res
    return wrapper


@log
def add(a, b):
    return a + b


print(add(1, 5))

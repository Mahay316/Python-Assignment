# 2. 编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中
from os import chdir
from datetime import datetime


# 定义带参装饰器
# file为日志文件的路径
def log(file='out.log'):
    def log_dec(func):
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            # 以追加方式打开日志文件
            with open(file, 'a', encoding='utf-8') as f:
                f.write(datetime.today().isoformat())
                f.write('\ninvoke function {0}'.format(func.__name__))
                f.write(' with args{0} and'.format(args))
                f.write(' keyword args{0}\n'.format(kwargs))
                f.write('return value: {0}\n'.format(ret))
            return ret
        return wrapper
    return log_dec


@log()
def add(a, b, *, doPrint=False):
    if doPrint:
        print(a + b)
    return a + b


chdir('Homework/homework5')
add(1, 2)
add(5, 10, doPrint=True)
add(2, 34)

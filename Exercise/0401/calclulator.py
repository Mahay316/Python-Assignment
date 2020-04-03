# 练习：定义高阶函数，实现计算器功能
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def dev(a, b):
    return a / b

# high-order function
def calc(a, b, op):
    return op(a, b)

print("{0} + {1} = {2}".format(4, 5, calc(4, 5, add)))
print("{0} + {1} = {2}".format(4, 5, calc(4, 5, sub)))

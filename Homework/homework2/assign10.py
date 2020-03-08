# 10. 编写一个函数calculate, 可以实现2个数的运算（加、减、乘、除）


# 强制使用关键字参数传入operation
def calculate(a, b, *, operation):
    "返回两个数的四则运算结果"
    if operation == 'ADD':
        return a + b
    elif operation == 'SUB':
        return a - b
    elif operation == 'MUL':
        return a * b
    elif operation == 'DEV':
        return a / b
    else:
        print("Error: Unsupportedd Operation")


print("3 + 4 =", calculate(3, 4, operation='ADD'))
print("20 * 5 =", calculate(20, 5, operation='MUL'))

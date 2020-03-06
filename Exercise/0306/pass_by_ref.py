# 测试Python函数参数传递的方式
def change(a):
    print("函数内修改前:", a)
    a.extend([1, 3, 5])
    print("函数内修改后:", a)
    print("函数内列表地址:", id(a))


b = [3, 4, 6]
print("函数外列表地址:", id(b))
change(b)
print("调用函数后: ", b)
print("函数外列表地址:", id(b))

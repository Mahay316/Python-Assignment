# 练习定义和调用函数的方法
def cal(weight, price):
    return weight * price


if __name__ == '__main__':
    weight = float(input("请输入苹果重量: "))
    price = float(input("请输入苹果单价: "))
    print("总价格为:", cal(weight, price))

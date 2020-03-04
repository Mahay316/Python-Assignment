# 使用input()函数接收输入的字符串
# 并根据空格分割后转换成元组
msg = input("Enter a string: ")
t = tuple(msg.split())
print(t)

# 接受输入并进行类型转换
weight = float(input("请输入购买苹果的重量(斤): "))
price = float(input("请输入苹果的单价(元/斤): "))
print("总价为%d元" % (weight * price))

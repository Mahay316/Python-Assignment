# 9. 设计一个猜数字游戏
# 最多只能猜测N次
# 在N次之内猜不出，就退出程序，提示猜测失败

from random import randint

# 最大猜测次数
N = 7
# 生成随机数
target = randint(0, 100)
print("输入一个[0, 100]的整数开始猜数字游戏")
for i in range(N):
    inp = int(input(f"第{i + 1}次猜测: "))
    if inp == target:
        print("恭喜猜测正确")
        break
    elif inp < target:
        print("猜小了")
    else:
        print("猜大了")
else:
    print(f"经过{N}次未猜中，猜测失败")

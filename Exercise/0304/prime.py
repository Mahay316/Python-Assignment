# 练习流程控制语句
# 判断数字是否为质数
for i in range(1, 10):
    for j in range(2, i):
        if (i % j == 0):
            print("{0} = {1} * {2}".format(i, j, i // j))
            break
    else:
        print(i, "is prime")

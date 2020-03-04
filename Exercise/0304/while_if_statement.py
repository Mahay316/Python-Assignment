# 练习流程控制语句
# 遍历输出列表中的偶数
a = [1, 3, 4, 6, 8, 9, 2, 0, 5, 8]
print("The content of list a:", a)
for i in a:
    if i % 2 == 0:
        print(i, end=' ')

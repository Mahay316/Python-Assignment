# 定义元组，并进行相关操作
score = (100, 89, 96, 76)
print(score + (88, 77, 'str'))
print(score * 3)
print("最高分:", max(score))
print("最低分:", min(score))
print("迭代输出:")
for x in score:
    print(x)

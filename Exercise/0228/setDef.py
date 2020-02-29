# 使用两种方式创建集合，并进行相应操作
set1 = {1, 2, 3}
set2 = set("mahay")
print(set1)
print(set2)
print(set1 | set2)

set2.discard('a')
print(set2)

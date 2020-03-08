# 1. 写函数判断用户传入的对象（字符串、列表、元组）长度
# 并返回给调用者


def length(obj):
    "返回传入对象的长度"
    return len(obj)


test_list = [1, 3, 5, 7, 9]
print("列表长度:", length(test_list))
print("字符串长度:", length("Test String"))
test_tuple = (3, 6, 8, 10)
print("元组长度:", length(test_tuple))

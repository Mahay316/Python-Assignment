# 2. 编写一个函数，接收n个数字，求这些参数数字的和


# 使用不定长参数
def get_sum(*nums):
    "返回传入数字之和"
    return sum(nums)


print("普通调用:", get_sum(1, 3, 5, 7, 9))
tup = (1, 2, 3, 4, 5, 6)
print("传入元组调用:", get_sum(*tup))

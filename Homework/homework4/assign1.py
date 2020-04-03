# 1. 定义一个10个元素的列表，通过列表自带的函数
# 实现元素在尾部插入和头部插入并记录程序运行的时间
# 用deque来实现，同样记录程序所耗费的时间
# 输出这2个时间的差值
# 提示：列表原生的函数实现头部插入数据：list.insert(0, v)、list.append(2)

from collections import deque
from time import perf_counter_ns  # 实现高精准度计时功能


ls = [i for i in range(10)]
dq = deque(ls)

# 测试在尾部插入元素，list性能更好
start = perf_counter_ns()
ls.append(20)
ls.append(30)
ls.append(40)
mid = perf_counter_ns()
dq.append(20)
dq.append(30)
dq.append(40)
end = perf_counter_ns()

print("尾部插入元素:")
print("list: {0}ns deque: {1}ns".format(mid - start, end - mid))
print("list - deque: {0}ns".format(2*mid - start - end))

# 测试在头部插入元素，deque性能更好
start = perf_counter_ns()
ls.insert(0, 20)
ls.insert(0, 30)
ls.insert(0, 40)
mid = perf_counter_ns()
dq.appendleft(20)
dq.appendleft(30)
dq.appendleft(40)
end = perf_counter_ns()

print("\n头部插入元素")
print("list: {0}ns deque: {1}ns".format(mid - start, end - mid))
print("list - deque: {0}ns".format(2*mid - start - end))

# 9. 定义一个函数，函数接收一个数组
# 并把数组里面的数据从小到大排序(冒泡排序，也可以直接使用相关的函数)


def bubble_sort(arr):
    "使用冒泡排序将列表元素从小到大排列"
    for i in range(len(arr) - 1):
        flag = True
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        if flag:
            break


test_list = [1, 5, 6, 7, 3, 2, 8, 0, 9, 4]
bubble_sort(test_list)
print(test_list)

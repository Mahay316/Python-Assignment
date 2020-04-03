# 8. 京东二面笔试题
# 1) 生成一个大文件ip.txt，要求1200行
#    每行随机为172.25.254.1 ~ 172.25.254.254之间的一个IP地址
# 2) 读取ip.txt文件统计这个文件中IP出现频率排前10的IP
from random import randint
from os import chdir


# 随机生成n个perfix网段的地址
# 存放到文件dst中
def rand_ip(prefix, dst, n):
    with open(dst, 'w', encoding='utf-8') as f:
        for _ in range(n):
            f.write(prefix + "." + str(randint(1, 254)))
            f.write('\n')


def count_ip(dst):
    # 使用hashmap计数
    dic = {}
    with open(dst, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n')
            if line in dic:
                dic[line] += 1
            else:
                dic[line] = 1

    # 返回排名前十的IP
    return sorted(dic.items(), key=lambda x: x[1], reverse=True)[:10]


chdir('Homework/homework4')
# rand_ip('172.25.254', 'ip.txt', 1200)
ips = count_ip('ip.txt')
print("出现频率前10的IP地址: ")
for item in ips:
    print("%-15s %2d" % item)

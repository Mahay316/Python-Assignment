# 10. 给定一段英文文本，统计每个单词出现的次数
# 打印输出，按照词频从高到低输出

# 提示：可以用字典来统计：key 是单词，value 是单词出现次数
# 先创建一个字典，然后遍历刚刚取出的单词列表，接着做一个判断
# 如果字典中key已经出现了这个单词，那么它对应的value，也就是出现次数就+1
# 如果这个单词没出现过，就直接插入这个单词及value为1到字典中
import re

para = input("输入一段英文文本，进行词频统计:\n")
# 使用正则分隔文本
words = re.split('[, .]', para)
freq = {}
for w in words:
    # 跳过空字符串
    if w == '':
        continue

    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

# 根据词频由高到低输出
print(" 单词           词频 ")
print("----------------------")
for k, v in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    print("%-15s %2d" % (k, v))

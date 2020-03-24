# 6. 在2个文件中存放了英文计算机技术文章(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章)
# 读取文章内容，进行词频的统计
# 并分别输出统计结果到另外的文件存放
# 比较这2篇文章的相似度
# 如果词频最高的前10个词，重复了5个，相似度就是50%，重复了6个，相似度就是60%，……

import os
import re


def get_freq(filename, stopwords):
    freq = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("找不到文件{0}，请检查文件名和路径的正确性".format(filename))
        raise  # 程序无法继续执行，重新抛出异常
    except IOError:
        print("无法打开文件{0}".format(filename))
        raise
    else:
        # 清除文本中的标点
        rep = re.compile('["“”,.:;_()\t\n]')
        content = rep.sub(' ', content)
        # 全部单词小写
        content = content.lower()
        # 简单分词
        words = content.split()
        # 词频统计
        for w in words:
            # 不统计停止词
            if w in stopwords:
                continue

            if w in freq:
                freq[w] += 1
            else:
                freq[w] = 1

    return freq


os.chdir('Homework/homework3')

file1 = 'built-in exception.txt'  # 第一篇文章
file2 = 'exception handling.txt'  # 第二篇文章
stop = 'stopwords.txt'  # 停止词文件，来自github
output = 'freq_out.txt'  # 词频统计结果输出文件

# 读取停止词，增加相似度判定准确度
# 集合的查找效率更高
sw = set()
try:
    with open(stop, 'r', encoding='utf-8') as f:
        for line in f:
            sw.add(line.strip('\n'))
except FileNotFoundError:
    print("找不到停止词文件{0}，请检查文件名和路径的正确性".format(stop))
    raise
except IOError:
    print("无法打开停止词文件{0}".format(stop))
    raise

# 将词频统计结果排序后保存到文件
freq1 = sorted(get_freq(file1, sw).items(), key=lambda x: x[1], reverse=True)
freq2 = sorted(get_freq(file2, sw).items(), key=lambda x: x[1], reverse=True)
try:
    with open(output, 'w', encoding='utf-8') as f:
        f.write("------ 文章1: {0} ------\n".format(file1))
        for k, v in freq1:
            f.write("%-18s %3d\n" % (k, v))
        f.write("\n------ 文章2: {0} ------\n".format(file2))
        for k, v in freq2:
            f.write("%-18s %3d\n" % (k, v))
except IOError:
    print("无法打开输出文件{0}".format(output))
    raise

# 计算两篇文章的相似度
top = 10  # 考察的高频词的数量
freq1 = freq1[:top]
freq2 = freq2[:top]

count = 0
for i, _ in freq1:
    for j, _ in freq2:
        if i == j:
            print(i)
            count += 1
print("文档相似度: %d%%" % (count / top * 100))

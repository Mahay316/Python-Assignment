# 8. 定义一个函数，给定一个字符串
# 找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数
# 例如，输入 aaaabbc，输出：a:4


def most_freq(string):
    # 记录出现次数最多的字符，可以免去排序的步骤
    max, res = 0, ''
    freq = {}
    for c in string:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

        if freq[c] > max:
            max = freq[c]
            res = c

    print("%s: %d" % (res, max))


most_freq("test text")
most_freq("aaaabbc")

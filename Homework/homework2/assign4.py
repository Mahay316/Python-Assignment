# 4. 写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符
# 并返回结果


# 返回格式(letter, number, space, other)
def count(string):
    "统计传入字符串的字母、数字、空格、其他字符的数量"
    letter, number, space, other = 0, 0, 0, 0
    for c in string:
        if c.isalpha():
            letter += 1
        elif c.isdigit():
            number += 1
        elif c == ' ':
            # 仅统计空格，将剩余空白字符视为其他字符
            space += 1
        else:
            other += 1

    return letter, number, space, other


test_str = "This \tis a string 4 testing."
print(count(test_str))

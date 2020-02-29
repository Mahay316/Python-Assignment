# 定义字符串，并进行查找子字符串，替换，计算长度等操作
a = 'Hello World'
print(a.index('ello'))
if a.find('ello') > 0:
    print('string snippet is in the string')
else:
    print('string snippet isn\'t in the string')
print(a.replace('ello', 'ola'))
print(f'length of \'{a}\' is', len(a))

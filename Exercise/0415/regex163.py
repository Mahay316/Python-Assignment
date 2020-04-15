# 练习: 使用正则表达式判断邮箱地址是否符合163或126格式
import re

regex = r'^[a-zA-Z0-9_]{4,20}@(163|126)\.com$'
ret = re.match(regex, 'hello@163.com')
print('匹配%s' % ('成功' if ret else '失败'))

ret = re.match(regex, 'regex_test@126.com')
print('匹配%s' % ('成功' if ret else '失败'))

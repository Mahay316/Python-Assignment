# 1. 给定一个文件
# 请用正则表达式逐行匹配提取其中的URL链接信息
# 将结果保存到另外一个文件中
# 提示：文件有1000行，注意控制每次读取的行数
import re
import os

# 切换工作目录
os.chdir('Homework/homework7')
# 网址以协议类型http或https开头
# 协议类型后接://
# 域名标号由文字和数字组成，标点符号只能使用-.
regex_str = r'((http|https)://[\w.-]*)'

count = 0
with open('webspiderUrl.txt', 'r', encoding='utf-8') as src:
    with open('assign1_urls.txt', 'a', encoding='utf-8') as dst:
        for line in src:
            urls = re.findall(regex_str, line)
            for url in urls:
                count += 1
                # 第一个group是完整的字符串
                dst.write(url[0])
                dst.write('\n')

print(f'提取了{count}个网址，输出到文件assign1_urls.txt')

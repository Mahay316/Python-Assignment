# 4. 爬取网址http://www.python3.vip/doc/prac/python/0001/
# 所有的Python练习题题目和答案
# 保存到txt文件中（只保留文字）
import requests
from bs4 import BeautifulSoup
from collections import deque


# 将题目和答案按一定格式保存到文件
# :param question 问题列表
# :param answer 答案列表
# :param filename 保存题目的文件
def record_exer(title, question, answer, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('**********' + title + '\n')
        for i in range(min(len(question), len(answer))):
            f.write('题目%d: ' % i)
            f.write(question[i] + '\n')
            f.write('答案:\n')
            f.write(answer[i] + '\n')

        # 分隔符
        f.write('*' * 40)
        f.write('\n')


header_data = {
    'content-type': 'text/html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 \
        Safari/537.36'
}
homepage = 'http://www.python3.vip/doc/prac/python/0001/'
exe_prefix = 'http://www.python3.vip/doc/prac/python/'
filename = 'assign4_exercise.txt'

visited = set()  # 链接去重
links = deque()  # 待访问链接
links.append(homepage)

while len(links) > 0:
    lk = links.popleft()
    if lk in visited:
        continue
    visited.add(lk)
    print(lk)

    try:
        # 获取html页面
        resp = requests.get(lk, headers=header_data, timeout=2)
    except IOError:
        continue

    html = resp.content.decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')

    # 记录所有习题页面
    exes = soup('a', href=lambda x: exe_prefix in x)
    exes = list(map(lambda x: x['href'], exes))
    links.extend(exes)

    title = soup.title.text
    ques = list(map(lambda x: x.text, soup('div', class_='content')))
    record_exer(title, ques, ques, filename)
    print(ques)
    break

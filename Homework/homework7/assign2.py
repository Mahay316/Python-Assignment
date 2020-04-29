# 2. 给定100个企业网站首页链接地址（用1中给出的URL地址）
# 请爬取每个页面上，企业介绍的链接地址
# 即标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址
# 提示：要用到requests、BeautifulSoup库
import re
import os
import requests
from bs4 import BeautifulSoup
from hashlib import md5
from collections import deque
from concurrent.futures import ThreadPoolExecutor, as_completed

header_data = {
    'content-type': 'text/html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 \
        Safari/537.36'
}


# 将链接处理成get()方法可以访问的形式
# 并将链接限制在本网站中，跨站的网址返回None
def process_link(homepage, lk):
    if lk != homepage and re.search(r'\.(png|gif|wav|js|css|jpg|ico)$', lk):
        return None  # 不访问其他类型的资源

    if not re.match('(http|https)://', lk):
        return homepage.rstrip('/') + '/' + lk.lstrip('/')
    elif homepage not in lk:
        # 拒绝跨站访问
        return None
    else:
        return lk


# 在指定网站中搜索标题为指定字符串的页面
# :param homepage 待搜索网站的首页
# :param keywords 搜索关键字列表
# :return 匹配到的页面url
def searchForTitle(homepage, keywords):
    print('accessing site:', homepage)
    # 使用集合保存已访问的网址，避免重复访问
    # 使用md5对网址进行散列再保存，减少内存占用
    visited = set(md5(homepage.encode('utf-8')).hexdigest())

    # 广度优先搜索，使用队列保存需要访问的网址
    links = deque()
    links.append(homepage)

    count = 0
    # 最多爬取300个网页，太深的页面是企业介绍的可能性很小
    while len(links) > 0 and count < 300:
        lk = links.popleft()
        if md5(lk.encode('utf-8')).hexdigest() in visited:
            continue  # 避免重复访问
        visited.add(md5(lk.encode('utf-8')).hexdigest())
        count += 1

        # 链接处理
        lk = process_link(homepage, lk)
        if not lk:
            continue  # 不访问跨站链接

        print('getting page', lk)
        try:
            resp = requests.get(lk, headers=header_data, timeout=2)
        except IOError:
            continue  # 超时等错误直接跳过

        # 请求成功则解析html
        if resp.status_code == 200:
            try:
                # 直接使用text获取内容将导致大部分网站产生乱码
                soup = BeautifulSoup(resp.content.decode('utf-8', 'ignore'),
                                     features='lxml')
            except BaseException:
                # 捕获所有异常，防止线程池中的线程崩溃
                print('处理', homepage, '时遇到异常')
                break

            a = soup('a', href=True)
            # 检索关键字
            for i in a:
                if i.string and any(map(lambda x: x in i.string, keywords)):
                    return (homepage, process_link(homepage, i['href']))

            # 找到所有页面中的所有链接加入队列
            a = map(lambda x: x['href'].strip(), a)
            links.extend(a)
    # 没找到介绍页面
    return (homepage, None)


keywords_list = [
    '企业介绍', '关于我们', '企业发展', '发展历史', '企业概况', '简介'
]
os.chdir('Homework/homework7')
tasks = []
# 使用线程池同时爬取多个网站
executor = ThreadPoolExecutor(max_workers=8)
with open('assign1_urls.txt', 'r', encoding='utf-8') as f:
    for i in range(100):
        tk = executor.submit(searchForTitle,
                             f.readline().strip('\n'), keywords_list)
        tasks.append(tk)

# 读取执行结果
with open('assign2_about.txt', 'w', encoding='utf-8') as f:
    for res in as_completed(tasks):
        data = res.result()
        print('about page url:', data[1])
        f.write(data[0] + ' -> ' + str(data[1]))
        f.write('\n')
        f.flush()

# 释放线程池资源
executor.shutdown()

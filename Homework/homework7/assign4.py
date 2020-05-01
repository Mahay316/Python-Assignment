# 4. 爬取网址https://www.programcreek.com/python/index/37/json
# 所有的Python示例程序
# 保存到txt文件中（只保留文字）
import os
import requests
from bs4 import BeautifulSoup


# 解析页面page中的示例程序代码
# 并将结果按一定格式写入文件filename
def parse_example(page, filename):
    print('parsing page:', page)
    try:
        resp = requests.get(page, headers=header_data, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        print('Exception occurs when parsing examples:')
        print(e)
        return

    page_soup = BeautifulSoup(resp.content.decode('utf-8'), features='lxml')
    exes = page_soup.find_all('pre', class_='prettyprint')
    title = page_soup.title
    # 如果没有找到示例程序，即exes为空列表，则直接返回
    if len(exes) == 0:
        print('page has no content!')
        return

    # 保存示例代码到文件
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(('*' * 20) + title.string + ('*' * 20) + '\n')
        for i, con in enumerate(exes):
            f.write('Example {}:\n'.format(i + 1))
            f.write(con.string)
            f.write('\n' + ('*' * 30) + '\n')
        f.write('\n')
    print('writing content to file {}'.format(filename))


header_data = {
    'content-type': 'text/html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 \
        Safari/537.36'
}
homepage = 'https://www.programcreek.com/python/index/37/json'
filename = 'assign4_example.txt'

links = set()  # 保存待访问的链接，用集合去重
try:
    resp = requests.get(homepage, headers=header_data)
    # 状态码不是200也抛出异常
    resp.raise_for_status()
except Exception as e:
    print('Exception occurs: {}'.format(e))
    os._exit(1)  # 程序退出

soup = BeautifulSoup(resp.content.decode('utf-8'), features='lxml')
# 解析出示例页的链接
lk = soup.find('ul', id='api-list').find_all('a', href=True)
for i in lk:
    links.add(i.attrs['href'])


os.chdir('Homework/homework7')
for page in links:
    parse_example(page, filename)
print('all done.')

# 3. 给定一个网址（包含了优质的英语学习音频文件）
# http://www.listeningexpress.com/studioclassroom/ad/
# 编写爬虫，将里面的英语节目MP3都下载下来
#
# 要求使用Requests库获取网页HTML文本内容
# 使用正则表达式获取所有mp3文件的网址
# 使用wget进行下载
import os
import re
import requests
import wget
from urllib.error import HTTPError

header_data = {
    'content-type': 'text/html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 \
        Safari/537.36'
}
link = 'http://www.listeningexpress.com/studioclassroom/ad/'

# 请求html页面
resp = requests.get(link, headers=header_data)
html = resp.content.decode('gb2312')

# 使用正则表达式获取所有MP3文件链接
# 使用set去重
result = set(re.findall(r'sc-ad[\w \'\\\-]*\.mp3', html))

os.chdir('Homework/homework7/assign3_files')
for i in result:
    # 去除特殊字符
    i = i.replace('\\', '')
    print('Downloading', i)
    try:
        wget.download(link + i)
        print()
    except HTTPError:
        print('文件{}下载失败'.format(i))

print('任务完成！')

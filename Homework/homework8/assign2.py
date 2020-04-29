# 2. 给定一组数据网址数据，请判断这些网址是否可以访问
# 用多线程的方式来实现
# 使用Python的requests库判断一个网址可以访问
import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


# 测试url可达性
# 可达返回True，超时、无法访问主机和状态码不是200均返回False
def test_connectivity(url):
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
    except requests.RequestException:
        # 无法访问
        return (url, False)
    return (url, True)


os.chdir('Homework/homework8')
tasks = []
# 由于网址过多，为每个网址分配一个线程开销过大
# 故使用线程池进行可达性测试
executor = ThreadPoolExecutor(max_workers=8)
with open('url_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        tasks.append(executor.submit(test_connectivity, line.strip('\n')))

ok, no = 0, 0
for future in as_completed(tasks):
    res = future.result()
    print(res[0], end='')
    if res[1]:
        ok += 1
        print('可访问')
    else:
        no += 1
        print('不可访问')

print('测试完毕，共%d个网址可访问，%d个网址不可访问' % (ok, no))
# 阻塞直到所有任务结束并释放资源
executor.shutdown()

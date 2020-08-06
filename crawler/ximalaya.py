"""
Download mp3 files from ximalaya
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pickle
import re
import random
import json
import requests
from queue import Queue
import ssl
import concurrent.futures
import time
from tqdm import trange

# ssl._create_default_https_context = ssl._create_unverified_context  #取消ssl认证s

#定义下载程序
def urllib_download(url,dirname, filename):
    from urllib.request import urlretrieve #这个是下载文件的库
    import os #这个是用于创建文件目录
    if not os.path.exists(dirname):  # 如果文件夹不存在，创建文件
        os.makedirs(dirname)
    filename = dirname + filename
    if os.path.exists(filename) == False:
        urlretrieve(url, filename)
    else:
        pass

#定义爬虫

def download(page_url,headers, page_num):
    pagedic = requests.get(page_url, headers=headers).text #获取这个字典
    pagedic = json.loads(pagedic)
    for i in trange(0,30):
        try:
            trackID = pagedic['data']['tracks'][i]['trackId']
            audio_url = 'https://www.ximalaya.com/revision/play/v1/audio?id={}&ptype=1'.format(trackID)
            audiodic = requests.get(audio_url, headers=headers).text  # 获取这个字典
            audiodic = json.loads(audiodic)
            src = audiodic['data']['src']  # 获取音频地址
            audio_name = str(page_num) + '_' + str(i)
        except:
            print('不能解析')
        else:
            print(src)
            zhang = (page_num - 1) * 30 + i + 1
            print('清朝大BUG  第' + str(zhang) + '章 下载完成')
            dirname = './' + str(page_num) + '/'
            filename = audio_name + '.m4a'  # 别忘记加上文件后缀名
            urllib_download(src, dirname, filename) #调用下载函数下载音频并命名



#定义 多进程方法

def multiprocessing(pages,headers, page_num):
    import multiprocessing as mp
    import time
    processes = []
    process_star_time = time.time()
    for page in pages:
        t = mp.Process(target=download,args=(page,headers,page_num,))#注意这里参数后面要有个逗号，不然报错
        processes.append(t)
    print(processes)
    for process in processes:
        process.start()
        print( '进程',process,'启动')
        process.join()
    processtime = '全部下载完成，多进程使用' + str(time.time() - process_star_time) + '秒'
    q.put(processtime)
#

if __name__ == "__main__":
    # 解析页面列表
    q=Queue()
    allpagenum = 10 # 总页数
    main_page = 'https://www.ximalaya.com/youshengshu/24362757/'  # \清朝大BUG
    headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'host': 'www.ximalaya.com',
    'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8', 'Accept-Encoding': 'gzip, deflate, br',
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Upgrade-Insecure-Requests': '1',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0'}
    session = requests.session()
    r = session.get(main_page, headers=headers)
    for page_num in range(7, allpagenum + 1):
        page_url = 'https://www.ximalaya.com/revision/album/v1/getTracksList?albumId=24362757&pageNum=' + str(page_num)
        # multiprocessing(page_url, headers, page_num)
        download(page_url, headers, page_num)


    # for i in range(1, 3):
    print(q.get())
    print('程序结束')

#全部下载完成，多进程使用1408.531194448471秒

# 程序结束





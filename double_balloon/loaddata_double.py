import requests
import csv
from bs4 import BeautifulSoup

# 开始与结束的期号
from_date = '03001'
to_date = '21003'
# URL以后可能会有变动
url = 'https://datachart.500.com/ssq/history/newinc/history.php?start={}&end={}'.format(from_date, to_date)
with open('double_ballon.csv', 'w', newline='') as csvfile:
    fieldnames = ['序号', '期号', 1, 2, 3, 4, 5, 6, 7, '时间']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    # 发送查询请求
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
    num = 0
    for content1 in soup.body.div.tbody.contents:
        if content1.name is not None:
            num += 1
            content2 = content1.contents
            writer.writerow({'序号': repr(num), '期号': content2[1].string, 1: content2[2].string, 2: content2[3].string,
                             3: content2[4].string, 4: content2[5].string, 5: content2[6].string,
                             6: content2[7].string, 7: content2[8].string, '时间': content2[16].string})




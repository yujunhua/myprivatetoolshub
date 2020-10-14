import requests
from bs4 import BeautifulSoup

# 开始与结束的期号
from_date = '07001'
to_date = '20100'
# URL以后可能会有变动
url = 'https://datachart.500.com/dlt/history/newinc/history.php?start={}&end={}'.format(from_date, to_date)
with open('dale.txt', 'w', newline='') as txtfile:
    # 发送查询请求
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
    num = 0
    for content1 in soup.body.div.tbody.contents:
        if content1.name is not None:
            num += 1
            content2 = content1.contents
            str1 = content2[2].string + ',' + content2[3].string + ',' + content2[4].string + ',' + \
                   content2[5].string + ',' + content2[6].string + ',' + content2[7].string + ',' + \
                   content2[8].string + '\n'
            txtfile.write(str1)





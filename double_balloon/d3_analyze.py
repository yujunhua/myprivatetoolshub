import csv
from matplotlib import pyplot as plt

# 绘图代码
x = []
y = []
with open('D3_num.csv', 'r') as csvfile2:
    plots = csv.reader(csvfile2, delimiter=',')
    for row in plots:
        if row[0] == '号码':
            continue
        x.append(int(row[0]))  #从csv读取的数据是str类型
        # print("x:",x)
        y.append(int(row[1]))
        # print("y:",y)

#画折线图
plt.figure(figsize=(20, 16), dpi=600)
plt.xticks(x, size='x-small', rotation=90, fontsize=1)
plt.yticks(y)
plt.bar(x, y, label='aa')
plt.xlabel('x')
plt.ylabel('y')
plt.title('bb')
plt.legend()
plt.savefig('1.png')
plt.show()


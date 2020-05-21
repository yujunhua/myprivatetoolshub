import os
import numpy as np

# 从文件中加载数据
def load_data():
    input_file = 'double_ballon.txt'
    with open(input_file, 'r') as f:
        data = f.readlines()

    return data

text = load_data()

# 定义一个矩阵，稍后填充

total_matrix = np.zeros((len(text), 7))

for ii, line in enumerate(text):
    content = line.strip().rstrip('\n').split(',')  # 分开每个数字
    total_matrix[ii, :] = content  # 填充矩阵

# 判断是否有两行相同的数字
times = 0
for iia in range(len(text)):
    # print('iia ', iia)
    for iib in range(len(text)):
        iib = iia + iib + 1  # 这里是为了防止重复比对
        times += 1
        if iib == len(text):
            break
        # 相同时，打印两行的索引
        if (total_matrix[iia] == total_matrix[iib]).all():
            print('iia ', iia, 'iib ', iib)
print(total_matrix.shape)
import os
import time
import numpy as np
from tqdm import trange

# 从文件中加载数据
def load_data():
    input_file = 'dale.txt'
    with open(input_file, 'r') as f:
        data = f.readlines()

    return data

"""
function: 比对数字
"""
def cacunums(firrow, secrow):
    nums = 0
    """
    红球和蓝球要单独对比
    """
    for fircol in range(5):
        for seccol in range(5):
            sub = total_matrix[firrow][fircol] - total_matrix[secrow][seccol]
            if sub == 0:
                nums += 1
                break

    for fircol in range(2):
        for seccol in range(2):
            sub = total_matrix[firrow][fircol + 5] - total_matrix[secrow][seccol + 5]
            if sub == 0:
                nums += 1
                break

    '''
    nums是相同数字的数目
    '''
    if nums == 4:
        print('\niia ', firrow + 1, 'iib ', secrow + 1)



text = load_data()

# 定义一个矩阵，稍后填充

total_matrix = np.zeros((len(text), 7))

for ii, line in enumerate(text):
    content = line.strip().rstrip('\n').split(',')  # 分开每个数字
    total_matrix[ii, :] = content  # 填充矩阵

start = time.clock()


# 判断是否有两行相同的数字

for iia in trange(len(text)):
    for iib in range(len(text)):
        if iia != iib:
            cacunums(iia, iib)

end = time.clock()
print("totla time : ", (end - start))
print(total_matrix.shape)
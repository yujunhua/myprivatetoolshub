import os
import numpy as np

# 从文件中加载数据
def load_data():
    input_file = 'double_ballon.txt'
    with open(input_file, 'r') as f:
        data = f.readlines()

    return data

"""
function: 比对数字
    type: "all" :全部数字."six","five",and so on .
"""
def cacunums(firrow, secrow, type="all"):
    nums = 0
    if type == 'all':
        # 相同时，打印两行的索引
        if (total_matrix[firrow] == total_matrix[secrow]).all():
            print('iia ', firrow, 'iib ', secrow)
    elif type == 'six':
        for ii in range(6):
            fircol = ii
            seccol = -1
            # 此处代码需改进，因为firow 的数字需要跟secrow的每个数字比
            while fircol != seccol:
                seccol += 1
                if seccol == 6:
                    break
                sub = total_matrix[firrow][fircol] - total_matrix[secrow][seccol]
                if sub == 0:
                    nums += 1

        if total_matrix[firrow][6] == total_matrix[secrow][6]:
            nums += 1
        if nums == 5:
            print('iia ', firrow + 1, 'iib ', secrow + 1)





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
        cacunums(iia, iib, 'six')
print(total_matrix.shape)
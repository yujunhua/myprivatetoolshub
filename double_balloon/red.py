# 只分析红球的出现次数，数据放入字典中
import csv


fieldnames = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0,
              17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0,
              32: 0, 33: 0}


with open('re.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    num = 1
    for row in reader:
        while num < 34:
            if int(row['1']) == num or int(row['2']) == num or int(row['3']) == num or \
                    int(row['4']) == num or int(row['5']) == num or int(row['6']) == num:
                fieldnames[num] += 1
            num += 1
        num = 1
    print(1, ':', fieldnames[1])
    print(2, ':', fieldnames[2])
    print(3, ':', fieldnames[3])
    print(4, ':', fieldnames[4])
    print(5, ':', fieldnames[5])
    print(6, ':', fieldnames[6])
    print(7, ':', fieldnames[7])
    print(8, ':', fieldnames[8])
    print(9, ':', fieldnames[9])
    print(10, ':', fieldnames[10])
    print(11, ':', fieldnames[11])
    print(12, ':', fieldnames[12])
    print(13, ':', fieldnames[13])
    print(14, ':', fieldnames[14])
    print(15, ':', fieldnames[15])
    print(16, ':', fieldnames[16])
    print(17, ':', fieldnames[17])
    print(18, ':', fieldnames[18])
    print(19, ':', fieldnames[19])
    print(20, ':', fieldnames[20])
    print(21, ':', fieldnames[21])
    print(22, ':', fieldnames[22])
    print(23, ':', fieldnames[23])
    print(24, ':', fieldnames[24])
    print(25, ':', fieldnames[25])
    print(26, ':', fieldnames[26])
    print(27, ':', fieldnames[27])
    print(28, ':', fieldnames[28])
    print(29, ':', fieldnames[29])
    print(30, ':', fieldnames[30])
    print(31, ':', fieldnames[31])
    print(32, ':', fieldnames[32])
    print(33, ':', fieldnames[33])

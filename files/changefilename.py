import os
import random


in_path = "D:\TMP\ml/tf\YOLOv3_TensorFlow\data\demo_data\myface\jpg1/"    # 目标路径
out_path = "D:\TMP\ml/tf\YOLOv3_TensorFlow\data\demo_data\myface\jpg/"
"""os.listdir(path) 操作效果为 返回指定路径(path)文件夹中所有文件名"""
filename_list = os.listdir(in_path)  # 扫描目标路径的文件,将文件名存入列表


# 打乱顺序重新命名
def changefilenamerandom(in_path, out_path, filename_list):
    num_list = list(range(1, 233))
    for filename in filename_list:
        used_name = in_path + filename
        ranint = random.randint(0, len(num_list)-1)  # 闭区间
        new_num = num_list[ranint]
        num_list.remove(new_num)     # 获取之后将之从listh中删除，防止重复
        new_name = out_path + str(new_num).zfill(6) + ".jpg"
        os.rename(used_name,new_name)
        print("%s ----->> %s" %(used_name, new_name))



# 按顺序命名
def changefilenameorder(in_path, out_path, filename_list):
    a = 1
    for i in filename_list:
        used_name = in_path + filename_list[a-1]
        new_name = out_path + str(a).zfill(6) + ".jpg"
        os.rename(used_name,new_name)
        print("文件%s重命名成功,新的文件名为%s" %(used_name,new_name))
        a += 1



if __name__ == '__main__':
    changefilenamerandom(in_path, out_path, filename_list)
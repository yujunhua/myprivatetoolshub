import os
import random
import pickle


in_path = "D:\TMP\ml/tf\YOLOv3_TensorFlow\data\demo_data\myface\jpg1/"    # 目标路径
out_path = "D:\TMP\ml/tf\YOLOv3_TensorFlow\data\demo_data\myface\jpg/"
xml_in_path = "D:\TMP\ml/tf\YOLOv3_TensorFlow\data\demo_data\myface/xml1/"
xml_out_path = "D:\TMP\ml/tf\YOLOv3_TensorFlow\data\demo_data\myface/xml/"
"""os.listdir(path) 操作效果为 返回指定路径(path)文件夹中所有文件名"""
filename_list = os.listdir(xml_in_path)  # 扫描目标路径的文件,将文件名存入列表

filename_dic = {}

# 批量修改文件后缀名
def changesuffixname(in_path, out_path, filename_list):
    for filename in filename_list:
        oldname_nojpg = filename[:-4]
        used_name = in_path + filename
        newname_nojpg = oldname_nojpg
        new_name = out_path + newname_nojpg + ".xml"
        os.rename(used_name,new_name)
        print("%s ----->> %s" %(used_name, new_name))

# 根据jpg文件的对应方式，修改xml文件命名
def changexmlnamebydic(in_path, out_path, filename_list):
    filename_loaddic = pickle.load(open('oldnewname_dic.p', mode='rb'))
    for filename in filename_list:
        oldname_nojpg = filename[:-4]
        used_name = in_path + filename
        newname_nojpg = filename_loaddic[oldname_nojpg]
        new_name = out_path + newname_nojpg + ".xml"
        os.rename(used_name,new_name)
        print("%s ----->> %s" %(used_name, new_name))

# 打乱顺序重新命名
def changefilenamerandom(in_path, out_path, filename_list):
    num_list = list(range(1, 233))
    for filename in filename_list:
        oldname_nojpg = filename[:-4]
        used_name = in_path + filename
        ranint = random.randint(0, len(num_list)-1)  # 闭区间
        new_num = num_list[ranint]
        num_list.remove(new_num)     # 获取之后将之从listh中删除，防止重复
        newname_nojpg = str(new_num).zfill(6)
        new_name = out_path + newname_nojpg + ".jpg"
        os.rename(used_name,new_name)
        filename_dic.update({oldname_nojpg: newname_nojpg}) # 老旧名存成字典，一遍xml文件对应修改
        pickle.dump(filename_dic, open('oldnewname_dic.p', 'wb')) # 字典的持久化
        print("%s ----->> %s" %(used_name, new_name))



# 按顺序命名
def changefilenameorder(in_path, out_path, filename_list):
    a = 1
    for i in filename_list:
        used_name = in_path + filename_list[a-1]
        new_name = out_path + str(a).zfill(6) + ".jpg"
        os.rename(used_name,new_name)
        print("%s ------>> %s" %(used_name,new_name))
        a += 1



if __name__ == '__main__':
    # changefilenamerandom(in_path, out_path, filename_list)
    # changexmlnamebydic(xml_in_path, xml_out_path, filename_list)
    changesuffixname(xml_in_path, xml_out_path, filename_list)
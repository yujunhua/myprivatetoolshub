"""
       功能： 把多个文件合并成一个，并在前面添加上 序号 和 所属图片 路径
 原文件格式：
            D:/TMP\000016.pts                                                     @文件路径

            |图片大小 |类别| 点坐标  |类别|  点坐标  |                               @说明
            800 1411   1  511 663    0    711 669                                 @文件内容

  生成格式：
            0 D:/TMP\000016.jpg 800 1411   1  511 663    0    711 669
            1 D:/TMP\000017.jpg ...
            ...
"""
import os

file_path = 'D:\TMP\ml/tf\YOLOv3_TensorFlow\data\demo_data\myface'
img_path = [os.path.join(file_path, 'jpg')]

train_path = [os.path.join(file_path, 'train_val/train_all.txt')]
test_path = [os.path.join(file_path, 'train_val/val_all.txt')]

gen_train_path = 'D:\TMP\ml/tf\YOLOv3_TensorFlow\data/demo_data/myface/train_val/train.txt'
gen_val_path = 'D:\TMP\ml/tf\YOLOv3_TensorFlow\data/demo_data/myface/train_val/val.txt'


def gen_train_txt(txt_path):
    train_cnt = 0
    f = open(txt_path, 'w')

    img_names = open(train_path[0], 'r').readlines()
    for img_name in img_names:
        objects = []
        img_name = img_name.strip()
        pts_path = img_path[0] + '/' + img_name + '.pts'
        pts_line = open(pts_path, 'r').readline()   # 读取一行
        if pts_line:
            jpgfile_name = img_path[0] + '/' + img_name + '.jpg'
            if os.path.exists(jpgfile_name):
                objects.append(str(train_cnt))
                train_cnt += 1
                objects.append(jpgfile_name)
                objects.append(pts_line)
                objects = ' '.join(objects)  # 以空格连接所有字符
                f.write(objects)
    f.close()


def gen_val_txt(txt_path):
    train_cnt = 0
    f = open(txt_path, 'w')

    img_names = open(test_path[0], 'r').readlines()
    for img_name in img_names:
        objects = []
        img_name = img_name.strip()
        pts_path = img_path[0] + '/' + img_name + '.pts'
        pts_line = open(pts_path, 'r').readline()   # 读取一行
        if pts_line:
            jpgfile_name = img_path[0] + '/' + img_name + '.jpg'
            if os.path.exists(jpgfile_name):
                objects.append(str(train_cnt))
                train_cnt += 1
                objects.append(jpgfile_name)
                objects.append(pts_line)
                objects = ' '.join(objects)  # 以空格连接所有字符
                f.write(objects)
    f.close()


if __name__ == '__main__':
    gen_train_txt(gen_train_path)
    gen_val_txt(gen_val_path)

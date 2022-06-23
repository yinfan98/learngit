import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

classes = ["person"]  # 改成自己的类别

def convert(size, box): #转换函数
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


def convert_annotation(image_id):
    in_file = open('C:/Users/ailink/Desktop/yolo_code/yolov5/first_data/Annotations/%s.xml' % (image_id), encoding='UTF-8') #打开xml的操作
    out_file = open('C:/Users/ailink/Desktop/yolo_code/yolov5/first_data/labels/%s.txt' % (image_id), 'w') #把打开的xml保存为txt文件 这一句和上面一句最后的%s.txt和%s.xml不用改 前面的地址需要改
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        # difficult = obj.find('Difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        b1, b2, b3, b4 = b
        # 标注越界修正
        if b2 > w:
            b2 = w
        if b4 > h:
            b4 = h
        b = (b1, b2, b3, b4)
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) )

data_path = 'C:/Users/ailink/Desktop/yolo_code/yolov5/first_data/images' #图片地址
img_names = os.listdir(data_path)

list_file = open('C:/Users/ailink/Desktop/yolo_code/yolov5/first_data/ImageSets/Main/val.txt', 'w') #改train的xml 就改地址到划分训练集的位置txt
for img_name in img_names:
    if not os.path.exists('C:/Users/ailink/Desktop/yolo_code/yolov5/first_data/labels'):
        os.makedirs('C:/Users/ailink/Desktop/yolo_code/yolov5/first_data/labels')#这里和上面改地址，这里的地址是保存label的路径

    list_file.write('C:/Users/ailink/Desktop/yolo_code/yolov5/first_data/images/%s\n' % img_name)#这里改地址，除了最后的%s\n前面改成你的图片地址
    image_id = img_name[:-4]
    convert_annotation(image_id)

list_file.close()


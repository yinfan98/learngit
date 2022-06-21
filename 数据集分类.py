import os
import cv2
import random
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
# os.makedirs('labels_train')
# os.makedirs('labels_val')

img_train_path ='C:/Users/ailink/Desktop/yolo_code/yolov5/first_data/train/images/'  #图片训练集保存路径，需要自己新建
img_val_path = 'C:/Users/ailink/Desktop/yolo_code/yolov5/first_data/val/images/'     #图片验证集保存路径   需要自己新建
#img_test_path =  'C:/Users/ailink/Desktop/image/test_2B/images/'  #图片测试集保存路径  ，需自己设置
labels_train_path = 'C:/Users/ailink/Desktop/yolo_code/yolov5/first_data/train/labels/'       #标签训练集保存路径   需要自己新建
labels_val_path = 'C:/Users/ailink/Desktop/yolo_code/yolov5/first_data/val/labels/'           #标签验证集保存路径   需要自己新建
#labels_test_path = 'C:/Users/ailink/Desktop/image/test_2B/labels/'
dir_images = 'C:/Users/ailink/Desktop/yolo_code/yolov5/first_data/images/'                       #数据集路径
dir_labels  = 'C:/Users/ailink/Desktop/yolo_code/yolov5/first_data/labels/'                  #标签路径

images = os.listdir(dir_images)             #把所有的图片名放入一个列表中
labels = os.listdir(dir_labels)            #labels的顺序和images的顺序不一定是一致的

random.seed(2022)                           #设置一个随机种子，确保每次运行都按照既定的随机形式
random.shuffle(images)                      #洗牌操作，打乱列表顺序

train_spilt_rate =0.8       #数据集划分比例，数据集较小可选0.8
a = int(len(images)*train_spilt_rate)   #训练集数量
count = 0
num_train=0
num_val =0
num_test = 0
for i,image in enumerate(images):   #对图片进行划分
    print(image)

    image_path = dir_images + image
    img = Image.open(image_path)    #读取图片
    if i < a:
        image = image.split('.')
        for label in labels:
            label = label.split('.')
            if label[0] ==image[0]:
                image = str.join('.',image)
                img.save(img_train_path + image)  # 保存训练集图像
                label = str.join('.',label)
                with open(dir_labels +label,'r') as f:
                    with open(labels_train_path + label , 'w') as s:    #保存训练集标签
                        s.write(f.read())
                num_train+=1
            else:
                continue
   
    elif i < int(len(images)*0.9):
        image = image.split('.')
        for label in labels:
            label = label.split('.')
            if label[0] == image[0]:
                image = str.join('.', image)
                img.save(img_test_path + image)  # 保存测试集
                label = str.join('.', label)
                with open(dir_labels + label, 'r') as f:
                    with open(labels_test_path + label, 'w') as s:  # 保存测试集
                        s.write(f.read())
                num_test+=1
    

    else :
        image = image.split('.')
        for label in labels:
            label = label.split('.')
            if label[0] == image[0]:
                image = str.join('.', image)
                img.save(img_val_path + image)  # 保存验证集
                label = str.join('.', label)
                with open(dir_labels + label, 'r') as f:
                    with open(labels_val_path + label, 'w') as s:  # 保存验证集
                        s.write(f.read())
                num_val += 1


            else:
                continue
    count+=1

print('图片总数量=====================',count)
print('测试集数量=====================',num_test)
print('训练集数量=====================',num_train)
print('验证集数量=====================',num_val)

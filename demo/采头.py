import cv2
import os
import glob

# 最后剪裁的图片大小
size_m = 112
size_n = 112


def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:, 2:] += rects[:, :2]
    return rects


cascade = cv2.CascadeClassifier("C:\\Users\\ailink\\.conda\\envs\\insightface\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml")
#imglist = glob.glob("C:/Users/ailink/Desktop/image/images_1A/*")
img = "C:/Users/ailink/Desktop/3.jpg"

img = cv2.imread(img) #for dir
dst = img
rects = detect(dst, cascade)
for x1, y1, x2, y2 in rects:
    roi = dst[y1 + 10:y2 + 20, x1 :x2+10]# 调整人脸截取的大小。横向为x,纵向为y
    img_roi = roi
    re_roi = cv2.resize(img_roi, (size_m, size_n))
    cv2.imwrite("C:/Users/ailink/Desktop/2_cut.jpg",re_roi)
'''
##############
##文件夹使用
##############
for list in imglist:

    # print(list)
    # cv2读取图像
    img = cv2.imread(list) #for dir
    dst = img
    rects = detect(dst, cascade)
    for x1, y1, x2, y2 in rects:
        # 调整人脸截取的大小。横向为x,纵向为y
        roi = dst[y1 + 10:y2 + 20, x1 + 10:x2]
        img_roi = roi
        re_roi = cv2.resize(img_roi, (size_m, size_n))

        # 新的图像存到data/image/jaffe_1
        f = "{}/{}".format("C:/Users/ailink/Desktop/image", "cut")
        # print(f)
        if not os.path.exists(f):
            os.mkdir(f)
        # 切割图像路径
        path = list.split("\\")
        print(path)
        # 新的图像存到data/image/jaffe_1   并以jpg 为后缀名
        cv2.imwrite("{}/{}/{}".format("C:/Users/ailink/Desktop/image", 'cut', path[1]), re_roi)
'''
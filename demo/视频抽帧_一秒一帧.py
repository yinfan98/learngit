import cv2
import numpy as np
import os
'''
for each vedio in videos
'''


SourceImgPath = "C:\\Users\\ailink\\Desktop\\video\\1A" + '\\'
Vedionamelist = os.listdir(SourceImgPath)

ImgWritePath = "C:\\Users\\ailink\\Desktop\\image\\1A" + '\\'
img_end = '.jpg'
img_start = 1

for vedio_path in Vedionamelist:
    VedioPath = os.path.join('%s%s' %(SourceImgPath, vedio_path))
    cap = cv2.VideoCapture(VedioPath)
    while cap.read():
        ret, frame = cap.read()
        if ret == False:
            break

        frames_num = cap.get(cv2.CAP_PROP_POS_FRAMES)
        # 显示实时帧数
        FPS = cap.get(cv2.CAP_PROP_FPS)
        # 总帧数
        total_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        # show information of frame
        # cv2.putText(frame, "FPS:"+str(FPS), (17, 13), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255))
        # cv2.putText(frame, "NUM OF FRAME:"+str(frames_num), (222, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255))
        # cv2.putText(frame, "TOTAL FRAME:" + str(total_frame), (504, 17), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255))
        # show a frame
        cv2.imshow("capture", frame)
        # img name

        # 存储
        if frames_num % 10 == 0:
            img_name = str(img_start) + img_end
            cv2.imwrite(ImgWritePath + img_name, frame)
            img_start = img_start + 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()







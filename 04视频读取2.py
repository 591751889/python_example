# 打开视频文件

import cv2
import numpy as np

cap = cv2.VideoCapture('video\\1111.mp4')

while (True):

    ret, frame = cap.read()  # 返回两个值，第一个为bool类型，如果读到帧返回True,如果没读到帧返回False,第二个值为帧图像

    if (ret):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('111', np.array(frame))
        cv2.waitKey(80)
        # print(np.array(frame),frame.shape)
        # print(type(gray))

    else:

        break

    if cv2.waitKey(1) == 27:
        break

cap.release()

cv2.destroyAllWindows()

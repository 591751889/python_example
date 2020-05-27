# 保存视频文件

import cv2

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 视频编码格式

out = cv2.VideoWriter('video\\1244.mp4', fourcc, 20, (640, 480))  # 第三个参数为帧率，第四个参数为每帧大小

cap = cv2.VideoCapture(0)

while (True):

    ret, frame = cap.read()

    if (ret):

        cv2.imshow('input', frame)

        out.write(frame)

    else:

        break

    if (cv2.waitKey(1) == 27):
        break

cap.release()

out.release()

cv2.destroyAllWindows()

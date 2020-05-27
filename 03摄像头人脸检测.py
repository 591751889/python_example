import numpy as np
import cv2

# 人脸识别分类器
faceCascade = cv2.CascadeClassifier(r'haarcascades/haarcascade_frontalface_default.xml')


# 开启摄像头
cap = cv2.VideoCapture(0)
ok = True

while ok:
    # 读取摄像头中的图像，ok为是否读取成功的判断参数
    ok, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 人脸检测
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(48, 48)
    )
    # 画矩形
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('video', img)

    k = cv2.waitKey(1)
    if k == 27:  # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
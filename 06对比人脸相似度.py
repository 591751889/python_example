import cv2
import face_recognition
import os
import xlwt
import datetime
writebook = xlwt.Workbook()

sheet = writebook.add_sheet('test',cell_overwrite_ok=True)

angelababy_image = face_recognition.load_image_file("photo/angelababy.jpg");#
angelababy_encoding = face_recognition.face_encodings(angelababy_image)[0]

guan_image = face_recognition.load_image_file("photo/guan.jpg");#
guan_encoding = face_recognition.face_encodings(guan_image)[0]

hua_image = face_recognition.load_image_file("photo/hua.jpg");#
hua_encoding = face_recognition.face_encodings(hua_image)[0]

jia_image = face_recognition.load_image_file("photo/jia.jpg");#
jia_encoding = face_recognition.face_encodings(jia_image)[0]

li_image = face_recognition.load_image_file("photo/li.jpg");#
li_encoding = face_recognition.face_encodings(li_image)[0]

lucas_image = face_recognition.load_image_file("photo/lucas.jpg");#
lucas_encoding = face_recognition.face_encodings(lucas_image)[0]

shen_image = face_recognition.load_image_file("photo/shen.jpg");#
shen_encoding = face_recognition.face_encodings(shen_image)[0]


shentao_image = face_recognition.load_image_file("photo/shentao.jpg");#
shentao_encoding = face_recognition.face_encodings(shentao_image)[0]

zheng_image = face_recognition.load_image_file("photo/zheng.jpg");#
zheng_encoding = face_recognition.face_encodings(zheng_image)[0]

unknown_image = face_recognition.load_image_file('photo/unknown.jpg');  # 无名suo人士
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([angelababy_encoding, guan_encoding, hua_encoding, jia_encoding,
                                                          li_encoding, zheng_encoding, lucas_encoding, shen_encoding,
                                                          shentao_encoding], unknown_encoding,tolerance=0.45)

for i in range(0, len(results)):
    if results[i] == True:
        print("相似的id是",i)

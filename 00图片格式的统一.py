


# -*- coding:utf-8 -*-

import os

from cv2 import cv2
import numpy as np

def listfilels(rootDir):
    list_dirs = os.walk(rootDir)
    # print("list_dirs", list_dirs)
    for root, dirs, files in list_dirs:
        # print("haoduo",root,dirs,files)
        # for d in dirs:
            # print('第一个', os.path.join(root, d))
        # print(type(files),len(files))
        for f in range(len(files)):
            # print("files",files[0])
            # fileId = files[f].split('.')[0]
            # print("fileid", fileId)
            filepath = os.path.join(root, files[f])
            try:
                # src = cv2.imread(filepath, 1)
                src = cv2.imdecode(np.fromfile(filepath, dtype=np.uint8), -1)
                # print("src=", filepath, src.shape)
                os.remove(filepath)
                # print("root", root)
                # print(filepath)
                gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
                cv2.imwrite(root + "\\" + str(f) + ".jpg", gray)  # r"C:\Users\29272\Desktop\111\1.jpg"
            except:
                # print('进入e')
                os.remove(filepath)
                continue


listfilels(r"C:\Users\29272\Desktop\1111")

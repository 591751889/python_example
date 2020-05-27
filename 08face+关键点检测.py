import cv2
import requests
import json
import base64

def file_base64(file_name):
    with open(file_name,'rb') as fin:
        file_data=fin.read()
        base64_data=base64.b64encode(file_data)
    return base64_data

url = 'https://api-cn.faceplusplus.com/humanbodypp/v1/detect'
filepath='photo/guan.jpg'
files = {'Image_file': open(filepath, 'rb')}
payload = {'api_key': 'TLTaqO4hSCZtNoxg4stjChq7o-0FPDYB',
           'api_secret': '9ptXes4ObjXHwHdjOVq-mekjoN-LlqRO',
           #'image_url': 'https://image.so.com/view?q=%E5%8D%83%E7%8E%BA&listsrc=sobox&listsign=c8f2dd5542c5c82c1e1116ad3425cce3&src=360pic_normal&correct=%E5%8D%83%E7%8E%BA&ancestor=list&cmsid=7cd680ddc9676663d354b03c861bf133&cmran=0&cmras=6&cn=0&gn=0&kn=50&fsn=130&adstar=0&clw=262#id=e8bfc493703e8be5669f2c133326a43f&currsn=0&ps=121&pc=121',
           'return_landmark': 1,
           'return_attributes': 'none',
           #'image_file':files,
          'image_base64': file_base64(filepath)
           }
r = requests.post(url, files=files, data=payload)
data = json.loads(r.text)

# %%
# print request content,you can also use r.+tab to see more things.
print(r.text)
a=str(r.text)
user_dict = json.loads(a)
print(user_dict.keys())
# for key in user_dict:
#     print(key+":"+str(user_dict[key]))
humanbodies=user_dict['humanbodies']
humanbody_rectangle=str(humanbodies[0])
print(humanbody_rectangle,type(humanbody_rectangle))
# new=json.loads(humanbody_rectangle)
# print(new )

#
# width = data['faces'][0]['face_rectangle']['width']
# top = data['faces'][0]['face_rectangle']['top']
# height = data['faces'][0]['face_rectangle']['height']
# left = data['faces'][0]['face_rectangle']['left']
# img = cv2.imread("12.jpg")
# vis = img.copy()
# # draw face rectangle
# # cv2.rectangle(vis, (left, top), (left+width, top+height),(0, 255, 0), 1)
#
# # %%
# # draw face landmarks
# for j in (0, len(data['faces']) - 1):
#     for i in data['faces'][j]['landmark']:
#         cor = data['faces'][j]['landmark'][i]
#         x = cor["x"]
#         y = cor["y"]
#         cv2.circle(vis, (x, y), 2, (0, 255, 0), -1)
# # %%
# cv2.imshow("Image", vis)
# cv2.waitKey(0)
# # save image with landmarks
# cv2.imwrite("Image", vis)
# cv2.destroyAllWindows()
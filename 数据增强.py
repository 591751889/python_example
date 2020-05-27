from keras.preprocessing.image import ImageDataGenerator,img_to_array,load_img
from PIL import Image
import matplotlib.pyplot as plt
import os
#需要改三处
pic_path='image'
augmentation_path='aferhighten'

data_gen=ImageDataGenerator(#图像数据发生器
          rotation_range=30,#旋转
          width_shift_range=0.1,#左右平移，图像的长宽小部分百分比为变化范围进行平移
          height_shift_range=0.1,#上下平移
          rescale=0.8,#对图像按照指定的尺度因子, 进行放大或缩小, 设置值在 0- 1 之间，通常为1 / 255
          shear_range=0.2,
          zoom_range=0.2,#随机放大或缩小
          horizontal_flip=True,
          fill_mode='nearest'#填充像素，出现在旋转或平移之后
)

for i in os.listdir(pic_path):
    img=Image.open(os.path.join(pic_path,i))
    rgb_im = img.convert('RGB')
    x=img_to_array(rgb_im)
    x=x.reshape((1,)+x.shape)
    if not os.path.exists(augmentation_path):
       os.makedirs(augmentation_path)
    n=1
    for batch in data_gen.flow(x,batch_size=1,save_to_dir=augmentation_path,save_prefix='1',save_format='jpg'):
        n+=1
        if n>7:
            break

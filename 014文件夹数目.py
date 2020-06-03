import os

os.chdir('datasets')#参数为路径
ls_file = []
ls_dir = []
for file in os.scandir():
 if file.is_dir():
  ls_dir.append(file.name)
 else:
  ls_file.append(file.name)
print("文件夹的总量是{}，\n文件分别为{}".format(len(ls_dir),ls_dir))



# coding=utf-8
import xlrd
import xlwt
import datetime

# readbook = xlrd.open_workbook('11.xls')

writebook = xlwt.Workbook()

sheet = writebook.add_sheet('test',cell_overwrite_ok=True) #第二个参数可以覆盖写
sheet.write(1,0,'result[0]')

writebook.save('folder/answer.xls')

sheet.write(1,0,'???')
writebook.save('folder/answer.xls')
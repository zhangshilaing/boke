import xlwt,datetime
workbook=xlwt.Workbook(encoding='utf-8')
worksheet=workbook.add_sheet('示例04')
# 获取字体样式对象
style=xlwt.XFStyle()
style.num_format_str='M/D/YY'
currentdatetime=datetime.datetime.now()
print(currentdatetime)
worksheet.write(0,0,currentdatetime) # 不设置日期时间格式，显示：43973.94252
worksheet.write(1,1,currentdatetime,style) # 设置日期时间格式：2020/5/22
workbook.save('E:/demo.xls')
print('写入Excel文件完成！')
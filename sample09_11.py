import xlwt
workbook=xlwt.Workbook(encoding='utf-8')
worksheet=workbook.add_sheet('示例02')
# 获取字体样式对象
style=xlwt.XFStyle()
# 获取字体对象
font=xlwt.Font()
font.name='微软雅黑'
font.bold=True  # 加粗
font.underline=True # 下划线
font.italic=True # 斜体
# 指定字体样式对象的字体属性为设置的字体对象
style.font=font
worksheet.write(0,0,'不带任何样式的文字')
worksheet.write(1,1,'使用带有样式的文字',style=style)
workbook.save('E:/demo.xls')
print('写入Excel文件完成！')
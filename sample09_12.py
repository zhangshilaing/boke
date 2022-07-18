import xlwt
workbook=xlwt.Workbook(encoding='utf-8')
worksheet=workbook.add_sheet('示例03')
# 设置单元格的宽度高度
worksheet.col(0).width=6666
worksheet.row(0).set_style(xlwt.easyxf('font:height 720'))
worksheet.write(0,0,'不带任何样式的文字')
workbook.save('E:/demo.xls')
print('写入Excel文件完成！')

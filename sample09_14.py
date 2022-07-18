import xlwt
workbook=xlwt.Workbook(encoding='utf-8')
worksheet=workbook.add_sheet('示例05')
worksheet.write(0,0,3)
worksheet.write(0,1,2)
# 给单元格设置公式
worksheet.write(1,0,xlwt.Formula('A1+B1'))
worksheet.write(1,1,xlwt.Formula('A1-B1'))
worksheet.write(2,0,xlwt.Formula('SUM(A1,B1)'))
worksheet.write(2,1,xlwt.Formula('SUM(A1,-B1)'))
workbook.save('E:/demo.xls')
print('写入Excel文件完成！')
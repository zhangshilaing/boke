import xlwt
workbook=xlwt.Workbook(encoding='utf-8')
worksheet=workbook.add_sheet('示例06')
# 给单元格添加超链接
worksheet.write(0,0,xlwt.Formula('HYPERLINK("http://www.taobao.com";"跳转至淘宝")'))
worksheet.write(1,1,xlwt.Formula('HYPERLINK("mailto://1728592651@qq.com";"写邮件给我")'))
workbook.save('E:/demo.xls')
print('写入Excel文件完成！')
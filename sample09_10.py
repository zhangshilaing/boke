# 日常工作中，使用Python输出数据给Excel文件
# 需要使用pip安装第三方模块：xlwt(Excel write 缩写)

# 设置pip国内镜像：
# 1、在当前操作系统的用户目录下（比如：Adminstator），新建一个目录：pip
# 2、在pip目录下，新建文件：pip.ini
# 3、在pip。ini文件中，编写如下内容：（如果出错，把内容中的注释去掉）
# [global]
# index-url = https://pypi.tuna.tsinghua.edu.cn/simple
# [install]
# trusted-host = https://pypi.tuna.tsinghua.edu.cn  # trusted-host 此参数是为了避免麻烦，否则使用的时候可能会提示不受信任
# 注意：如果进行pip install操作时，看见提示信息有：Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple，说明设置成功

# 常用的pip命令:
# 1、pip list ：查看安装的模块信息（包括模块名称和模块版本）
# 2、pip install 模块名称：安装某个模块
# 3、pip uninstall 模块名称：卸载某个模块
# 4、pip help：查看pip的帮助
# 5、python -m pip install --upgrade pip：对pip自身的升级

import xlwt
# 步骤1：创建一个workbook对象（Excel的文件对象）并设置一个编码格式
workbook=xlwt.Workbook(encoding='utf-8')
# 步骤2：创建一个sheet对象（Excel的sheet对象）
worksheet=workbook.add_sheet('示例01')
# 步骤3：向sheet写入内容
# write(r,c,lable='')函数：excel文件的sheet对象的写函数
# 常用参数：r：行
#         c：列
#         lable：内容
worksheet.write(0,0,label='这是第一个示例')  # 在Excel文件的第一行第一列写入内容
# 步骤4：把内存中的excel的workbook对象持久化存储成文件
workbook.save('E:/demo.xls')
print('写入Excel文件完成！')



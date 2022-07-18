# 1、Python语言：荷兰人Guido van Rossum（吉多.范.罗素姆）1989年发明，1991年正式发布，官网：https://www.python.org
# 2、Python语言特点：简单易用的偏向解释型的语言
# 编译型语言 和 解释型语言：
# ① 编译型语言：C语言
# ② 解释型语言：Ruby语言
# 计算机是不能理解高级语言，也不能直接执行基于高级语言编写的代码文件，只能直接理解机器语言，因此使用高级语言编写的程序想被计算机执行，必须先将其转换成计算机语言，就是所谓的机器码
# ① 编译型语言：使用编译器，将程序文件的代码编程为机器语言（部分编译型语言会生成中间字节码，运行在对应的虚拟机环境中），被计算机硬件执行
# 特点：编译型首先编译为二进制文件，所以在执行时速度相对较快
# ② 解释型语言：使用解释器，在执行时，对程序文件的代码做解释执行
# 高级语言发展至今，对于编译型语言和解释型语言的界定不再那么苛刻，以Python为例，描述其为偏向解释型的语言，因为对于Python语言，执行时，解释器同时做了编译和解释两项工作
# （.py代码文件首先被解释器编译为.pyc字节码文件，再在pvm运行时环境中做解释执行）
# 特点：解释型在执行时才去做编译和解释的工作，所以在执行时速度相对较慢
#
# 3、Python语言版本：曾经长期存在两个大版本，Python 2 和 Python 3，因为Python 3是趋势，所以我们学习的是Python 3
#
# 4、Python 3的环境搭建：
# ① 下载Python 3的安装文件，Python 3的版本说明：
# 针对64位操作系统：
# Windows x86_64 embeddable zip file：嵌入式版本，可以集成到其他的应用中
# Windows x86_64 executable installer：可执行文件(.exe)版本
# Windows x86_64 web-based installer：基于网络安装版本
# 针对32位操作系统：
# Windows x86 embeddable zip file：嵌入式版本，可以集成到其他的应用中
# Windows x86 executable installer：可执行文件(.exe)版本
# Windows x86 web-based installer：基于网络安装版本
# ② Python 3安装：（建议安装过程出现的信息都读一读，知道到底安装了什么）
# 在命令行窗口中，输入python -V，能够看到Python的版本信息，说明安装成功
# ③ 思考：为什么Python指令可以在命令行窗口中被执行？
# 环境变量：由变量名 和 变量值组成（一个变量名对应多个变量值，多个变量值之间使用英文的逗号分隔开）
# Path路径环境变量：（干净的刚安装完毕的操作系统有如下四项）
# %SystemRoot%\system32;
# %SystemRoot%;
# %SystemRoot%\System32\Wbem;
# %SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;
# 这里的SystemRoot指的是Window操作系统默认安装路径：C:\Windows
# 上面的四个路径其实就是告诉操作系统，当输入某个指令时，到这些路径所对应的目录中查找是否有内部命令或外部命令或可执行程序或批处理文件
# 显然得知，在Python3的安装过程中，如果忘记了勾选添加Python路径到Path环境变量的话，可以手动添加D:\Python3\Scripts\;D:\Python3\;添加到Path环境变量中
#
# 5、编码
# ① ASCII码：表示英数字符
# ② GBK码：对ASCII码的补充，包含中日韩文字
# ③ Unicode码：万国码
# ④ UTF8码、UTF16码、UTF32码：可变长度的Unicode码
# 编程时要求使用UTF8码
#
# 6、Python开发工具的选择：
# ① 默认安装时自带了IDLE，功能有限可以应急
# ② 推荐使用Pycharm，功能强大
#
# 7、Pycharm的常用设置：Default Settings中做设置
# ① Editor中找到File encodings，把工程以及配置文件的编码均设置为utf-8
# ② Editor中找到File and code templates，找到Python Script，去掉作者说明的注释
# ③ Default Project中设置Project Interpreter，找到前面Python3安装的路径即可
# ④ Editor中找到General，找到Apprearance，找到show line numbers，显示行号
# ⑤ Editor中找到General，找到Code Completion，设置Case sensitive completion为None
# ⑥ Editor中找到Colors and Fonts，找到Font，另存一份配置进行编辑，写代码使用等宽字体，选择consolas
#
# 8、python的注释形式：
# ① 单行注释，以英文 # 开头，后面的内容都是注释内容
# ② 多行注释（段注释），以一对三个连续的英文单引号 '''包裹起来形成多行注释

# 第一个Python程序
'''
使用print()函数输出一个字符串
'''
print("Python很简单")  # Python很简单

 # 编码规范
 # 1、代码编写后进行格式化，保证代码整洁（Pycharm默认格式化快捷键：ctrl+alt+L）
 # 2、代码中的命名追求“见名知意”的原则
 # 3、自定义的模块名或包名，使用全小写字母，名称尽量简洁，如果涉及多个单词，多个单词之间使用英文下划线_进行连接，比如：spec_module
 # 4、自定义的函数名，使用全小写字母，名称尽量简洁，如果涉及多个单词，多个单词之间使用英文下划线_进行连接，比如：calc_salary
 # 5、自定义的类名，使用首字母大写，采用camel驼峰命名，如果涉及多个单词，每个单词首字母大写，比如:ClassName
 # 6、常量名，使用全部字母大写，如果涉及多个单词，多个单词之间使用英文下划线_进行连接，比如：MAX_VALUE



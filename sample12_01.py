# TCP/IP模型：（自顶向下）四层或五层
# 应用层、传输层、网际层、网络接口层（数据链路层，物理层）
# 其中，TCP、UDP处于传输层，IP协议处于网络层
# IP协议：基本功能是分段和寻址
# 给网络硬件设备分配唯一标识，IPv4和IPv6
# 环回地址（回送地址）：特殊的IP地址，127.0.0.1，指向的是本机，用于网络测试和本地进程间通信
# 使用环回地址发送数据，不会进行网络传输，只在本机的进程间进行通信
# 端口：网络硬件设备上有多个通信程序运行时，需要提供不同的端口进行通信，类比：医院和站台窗口
# Socket：套接字，进行网络通信的两个程序之间，通过一个双向的通信链路，连接起来进行数据交换，位于这个通信链路两端的部分称为套接字Socket
# CS架构：Client（客户端）和 Server（服务端）
# UDP协议：面向无连接的通信，类比：生活中的写信

# UDP Socket 通信过程：
# 1、服务端绑定IP地址和端口
# 2、客户端设置要发送的数据给指定的服务端的IP和端口
# 3、服务端接收客户端发送的数据
# 4、关闭Socket对象，释放资源

import socket
def main():
    # -----UDP服务端------
    # 获取Socket对象
    # Socket对象的构造函数的参数说明：family：默认值为AF_INET，表示IPv4；如果使用IPv6，则设置为AF_INET6
    #                              type:默认值为SOCK_STREAM,流式套接字用于TCP通信；如果使用UDP通信，则使用SOCK_DGRAM
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 服务端绑定IP地址和端口
    s.bind(('192.168.1.11',1234))
    print('UDP服务端启动·····')
    # 服务端接收客户端发送的数据
    while True:
        data=s.recvfrom(1024)
        # print(data)
        # 需要在客户端对数据内容进行编码，在服务端对数据内容进行解码
        print('IP地址【{0}】的端口【{1}】，发送数据：{2}'.format(data[1][0], data[1][1], data[0].decode()))
    # 关闭Socket对象，释放资源
    s.close()
main()

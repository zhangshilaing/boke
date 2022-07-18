# TCP协议：面向连接的通信，类比：生活中的打电话
# TCP一旦建立，会一直占用，直到关闭连接为止

# TCP Socket通信过程：
# 1、服务端绑定IP地址和端口
# 2、服务端监听端口
# 3、服务端等待客户端发送连接请求
# 4、客户端设置要连接服务端的IP地址和端口
# 5、客户端发送连接请求
# 6、服务端接受客户端发送的连接请求，建立起连接
# 7、客户端和服务端双向发送数据 或 接收数据
# 8、关闭连接
# 9、关闭Socket对象，释放资源

import socket
def main():
    # -----TCP服务端------
    # 获取Socket对象
    # Socket对象的构造函数的参数对象：family：默认值为AF_INET，用于IPv4；如果使用IPv6，则为AF_INET6
    #                              type：默认值为SOCK_STREAM，流式套接字TCP通信；如果用于UDP通信，则为SOCK_DGRAM
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 服务端绑定IP地址和端口
    s.bind(('192.168.1.11',1234))
    # 服务端监听端口
    s.listen()

    print('TCP服务端启动·····')

    # 创建连接：
    conn,addr=s.accept()
    print('IP地址【{0}】的端口【{1}】'.format(addr[0],addr[1]))
    # 服务端接收客户端发送的数据
    while True:
        data=conn.recv(1024)
        # 需要在客户端对数据内容进行编码，在服务端对数据内容进行解码
        print('发送数据：{0}'.format(data.decode()))

    # 关闭连接
    conn.close()

    # 关闭Socket对象，释放资源
    s.close()

main()
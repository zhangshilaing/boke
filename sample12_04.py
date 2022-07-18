import socket
def main():
    # ----TCP服务端------
    # 获取Socket对象
    # Socket对象的构造函数的参数说明：family：默认值为AF_INET，用于IPv4；如果用于IPv6，则为AF_INET6
    #                                type：默认值为SOCK_STREAM，流式套接字用于TCP通信；如果用于UDP通信，则为SOCK_DGRAM
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 客户端发送连接请求
    s.connect(('192.168.1.11',1234))

    print('TCP客户端启动····')

    while True:
        data=input()
        # 需要在客户端对数据进行编码，在服务端对数据进行解码
        s.send(data.encode())

    # 关闭Socket对象，释放资源
    s.close()

main()

import socket
def main():
    # ------UDP客户端-----
    # 获取Socket对象
    # Socket对象的构造函数的参数说明：family：默认值为AF_INET,表示IPv4；如果使用IPv6，则为AF_INET6
    #                               type：默认值为SOCK_STREAM，流式套接字TCP通信；如果用于UDP通信，则使用SOCK_DGRAM
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print('UDP客户端启动···')
    while True:
        data=input()
        s.sendto(data.encode(),('192.168.1.11',1234))

        if data=='exit':
            break

    # 关闭Socket对象，释放资源
    s.close()
main()


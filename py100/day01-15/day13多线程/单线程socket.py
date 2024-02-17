import socket


def send_request(host, port=80):
    # 创建套接字对象
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接
    client_socket.connect((host, port))
    # 发送HTTP GET请求
    request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    client_socket.send(request.encode())

    # 接收响应头
    response = b""
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        response += data

    # 关闭连接
    client_socket.close()
    return response.decode("utf-8").rstrip()


if __name__ == "__main__":
    hosts_list = ['www.sina.com.cn', 'www.sohu.com', 'www.baidu.com', 'www.163.com']
    for host in hosts_list:
        print('----------------------------------------------------   {} header'.format(host))
        response = send_request(host)
        print(response)

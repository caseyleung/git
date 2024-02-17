"""
文件相关的工具模块
"""


def print_file_info(file_name):
    """
    将给定路径的文件内容全部读取出来
    :param file_name: 文件的路径
    :return: None
    """
    f = None
    try:
        f = open(file_name, 'r', encoding='UTF-8')
        content = f.read()
        print(f"文件的全部内容如下：{content}")
    except Exception as e:
        print(f"程序出现异常了，原因是：{e}")
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    """
    把数据追加到指定的文件中
    :param file_name: 文件的路径
    :param data: 追加的内容
    :return: None
    """
    f = open(file_name, 'a', encoding='UTF-8')
    f.write('\n')
    f.write(data)
    f.close()


if __name__ == '__main__':
    print_file_info(r"/stageOne/py.txt")
    # append_to_file(r"C:\Users\CaseyL\Desktop\pylearn\py.txt", "这是条测试")

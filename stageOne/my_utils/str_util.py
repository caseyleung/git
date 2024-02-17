"""
字符串相关的工具模块
"""

def str_reverse(s):
    """
    将字符串完成反转
    :param s: 将被反转的字符串
    :return: 反转后的字符串
    """
    return s[::-1]


def substr(s, x, y):
    """
    按照给定的下标完成给定的字符串切片
    :param s: 被切片的字符串
    :param x: 开始下标
    :param y: 结束下标
    :return: 完成的字符串
    """
    return s[x:y]



if __name__ == '__main__':
    print(str_reverse("hello ,spongebob"))
    print(substr("spongebob", 6, 99))


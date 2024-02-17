"""
函数的初体验
"""

# str = "hello,"
# str2 = "python"
# str3 = "netease"
#
# print(len(str))
#
# def my_len(data):
#     count = 0
#     for i in data:
#         count += 1
#     print(f"字符串{data}的长度是{count}")
#
# my_len(str)
# my_len(str2)
# my_len(str3)


"""
函数的定义
"""


# def my_add(x, y):
#     print(f"{x + y}")
#
#
# my_add(2, 3)
# my_add(12, 3)
# my_add(2, 13)


def check_age(age):
    if age > 18:
        return "success"
    else:
        return None


result = check_age(16)
if result is None:
    print("未成年，不可以进入")

if not result:
    print("未成年，不可以进入")

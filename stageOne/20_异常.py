"""
try:
    可能发生错误的
except:
    如果出现异常执行的
else:
    没有异常的时候执行的
finally:
    无论如何都会执行的
"""

"""
捕获常规异常
"""

# try:
#     f = open(r'C:\Users\CaseyL\Desktop\bb.txt', 'r', encoding="UTF-8")
# except:
#     print(f"出现异常了，因为文件不存在")
#     f = open(r'C:\Users\CaseyL\Desktop\bb.txt', 'w', encoding="UTF-8")
#

"""
捕获指定异常
"""

try:
    1 / 0
except ZeroDivisionError as e:
    print(f"捕获指定异常: {e}")

try:
    print(name)
except NameError as e:
    print(f"捕获指定异常: {e}")

"""
捕获多个异常
"""
print()
try:
    1 / 0
    # print(name)
except (ZeroDivisionError, NameError) as e:
    print(f"捕获多个异常: {e}")

"""
捕获全部异常
"""
print()
try:
    f = open(r'C:\Users\CaseyL\Desktop\bb.txt', 'r', encoding="UTF-8")
except Exception as e:
    print(f"捕获全部异常: {e}")
else:
    print("啊，好高兴，没有出现异常")
finally:
    print("给我执行！")

"""
异常具有传递性
"""
print()
def fun1():
    print("fun1 开始执行")
    num = 1/0
    print("fun1 结束")

def fun2():
    print("fun2 开始执行")
    fun1()
    print("fun2 结束")

def main():
    try:
        fun2()
    except Exception as e:
        print(f"捕获到的异常：{e}")

main()
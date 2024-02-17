"""
编码就是一种规则集合，记录了内容和二进制间进行相互转换的逻辑
计算机中有许多可用编码： UTF-8(全球通用), GBK(中文)...
"""
import time

"""
文件操作：打开、读、写、关闭
"""

# 打开文件  open(filename, mode, encoding=None)

# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
# 原因：因为这样 "C:\Users\CaseyL\Desktop\pylearn\19_文件.py" 的写法会转义
# 解决办法： 1. 换成反斜杠 / ; 2. 双斜杠 \\ ; 3. 前面加个r，eg: r"C:\Users\CaseyL\Desktop\test.txt"

f = open(r'/stageOne/py.txt', "r", encoding="UTF-8")
print(type(f))

# 读取文件 read()
# print(f"读取10个字节的结果：{f.read(10)}")
# print(f"读取全部内容的结果：{f.read()}")

# 读取文件 readlines()
# lines = f.readlines()
# print(f"lines对象的类型是：{type(lines)}, 内容是: {lines}")

# 读取文件 readline()
# line1 = f.readline()
# line2 = f.readline()
# print(f"line对象的类型是：{type(line1)}, 内容是: {line1}")
# print(f"line对象的类型是：{type(line2)}, 内容是: {line2}")

# for line in open(r'C:\Users\CaseyL\Desktop\pylearn\py.txt', encoding="UTF-8"):
#     print(line)


# 关闭文件 close
f.close()
# time.sleep(5000)


# with open 操作文件。运行完成后自动关闭
with open(r'/stageOne/py.txt', encoding="UTF-8") as f:
    for line in f:
        print(line)

# 文件不存在会被创建出来
# f = open(r'F:\py.txt', "w", encoding="UTF-8")
# 写文件 write
# f.write("hello, world")
# f.write("\n1111")
# f.flush()
# f.close() # 带有flush()的功能


# 如果文件已经存在，再次打开写入里面的内容会被清空
# f = open(r'F:\py.txt', "w", encoding="UTF-8")
# f.write("hhhhh")

# 写入文件 mod: a。文件不存在会被创建，存在后在后面写入文件
f = open(r'F:\py.txt', "a", encoding="UTF-8")
f.write("\nhello, world")
f.close()

f = open(r'C:\Users\CaseyL\Desktop\xx.txt', 'a', encoding="UTF-8")
f.write("写一百个jack")

for i in range(1,100):
    f.write('jack\n')

f.close()
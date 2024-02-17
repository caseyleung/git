"""
模块导入方式：
[from module name] import [module | class | variable | function | *] [as alias]
"""

# import time
# time.sleep(100)
#
# #使用from导入time的sleep功能
# from time import sleep
# sleep(100)
#
#
# # 导入time模块的全部功能
# from time import *
# sleep(100)
#
# # 使用as给模块加上别名
# import time as t
# t.sleep(100)
#
#
# # 使用as给特定功能加上别名
# from time import sleep as sl
# sl(100)

"""
自定义模块
"""
import hello

hello.hello()
hello.test(1, 3)
hello.test2(3, 1)

# __main__ 变量
# 只有当程序是直接执行的才会进入if内部，如果是被导入的，则if无法进入


# __all__ 变量
# 控制 import * 能够导入的内容
from hello import *
hello.test2(3,1)


"""
python包就是一个python文件夹，里面包含一个__init__.py文件，该文件夹下包含多个模块文件。从逻辑上看，包的本质依然是模块。
包的作用：当我们的模块文件越来越多时，包可以帮助我们管理这些模块，
"""

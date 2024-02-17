"""
演示python包
"""
# 导入自定义包的模块并使用
# import my_package.my_module1
# import my_package.my_module2
#
# my_package.my_module1.info_print1()
# my_package.my_module2.info_print1()

# from my_package import my_module1
# from my_package import my_module2
# my_module1.info_print1()
# my_module2.info_print1()

# from my_package.my_module1 import info_print1 as print1
# from my_package.my_module2 import info_print1 as print2
# print1()
# print2()

"""
安装第三方的包，在python程序的生态中，有许多非常多的第三方包（非官方），可以极大的帮助我们提高开发效率，如：
科学计算中常用的：numpy包
数据分析中常用的：pandas包
大数据计算中常用的：pyspark包、apache-flink包
图形可视化常用的：matplotlib、pyecharts
人工智能常用的：tensorflow
...
但是由于是第三方，所以python没有内置，所以需要安装它们才可以导入使用

安装第三方包 - pip（python内置的）
- pip install 包名称
- pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称
- pip install 包名称 -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
- pip install pyecharts -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
- pip install pymysql -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
- pip install pyspark -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
- pip install psutil -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
- pip install matplotlib -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
- pip install pygame -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

把pip全局换成清华源: 在cmd输入 pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

"""

from my_utils import str_util
from my_utils import file_util

content = "长洲宾客人数多"
content1 = str_util.str_reverse(content)
content2 = str_util.substr("spongebob", 0, 6)
print(f"str_util包的方法测试结果:\n{content1} \n{content2}")

print()
file_name = r"/stageOne/py.txt"
file_util.append_to_file(file_name, content)
file_util.append_to_file(file_name, content1)
file_util.append_to_file(file_name, content2)
print('--------------------------')
file_util.print_file_info(file_name)



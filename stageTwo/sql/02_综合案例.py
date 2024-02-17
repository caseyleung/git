from stageTwo.数据分析案例.file_define import TextFileReader, JsonFileReader
from stageTwo.数据分析案例.data_define import Record

cvs_file_reader = TextFileReader(r"C:\Users\CaseyL\Desktop\pylearn\stageTwo\数据分析案例\2011年1月销售数据.cvs")
json_file_reader = JsonFileReader(r"C:\Users\CaseyL\Desktop\pylearn\stageTwo\数据分析案例\2011年2月销售数据.json")

jan_data: list[Record] = cvs_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

all_data: list[Record] = jan_data + feb_data

for line in all_data:
    print(line)


"""
自建的module包所在路径不在PYTHONPATH下
适用场景： 自建的包找不到

在IDE中执行python程序，编译器会自动把当前项目的根目录加入到包查找路径中，可以理解为加到PYTHONPATH下，所以直接执行是没有问题的。但是在cmd或者terminal控制台中直接使用python相关命令来执行程序，不会自动将当前项目加入到PYTHONPATH环境变量下，如果涉及到import其他文件夹下的变量就会报类似ImportError: No module named xxx这样的错误。

解决方法是使用sys.append()命令把报警包的所在文件夹路径加入到PYTHONPATH。
————————————————
版权声明：本文为CSDN博主「Lucky小黄人」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_41767116/article/details/119988991
"""


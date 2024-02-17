
"""
面向对象，数据分析案例，主业务逻辑代码
实现步骤：
1.设计一个类，可以完成数据的封装
2.设计一个抽象类，定义文件读取相关功能，并使用子类实现具体功能
3.读取文件，生成数据对象
4.进行数据需求的逻辑计算
5.通过pyecharts进行图形绘制
"""

from file_define import TextFileReader, JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import *

cvs_file_reader = TextFileReader(r"C:\Users\CaseyL\Desktop\pylearn\stageTwo\数据分析案例\2011年1月销售数据.cvs")
json_file_reader = JsonFileReader(r"C:\Users\CaseyL\Desktop\pylearn\stageTwo\数据分析案例\2011年2月销售数据.json")

jan_data: list[Record] = cvs_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

all_data: list[Record] = jan_data + feb_data


data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# print(data_dict)

bar = Bar(init_opts=InitOpts(width="2200px", height="1200px", page_title="销售额柱状图", theme=ThemeType.LIGHT))

bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(position="top"))
bar.set_global_opts(
    title_opts=TitleOpts(is_show=True, title="每日销售额")
)

bar.render("销售额柱状图.html")



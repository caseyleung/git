"""
演示可视化：折线图
"""
import json
from pyecharts.charts import Line
from pyecharts.globals import ThemeType
from pyecharts.options import *


f_us = open(r"C:\Users\CaseyL\Desktop\pylearn\stageOne\23_可视化\lineChart\America.json", "r", encoding="UTF-8")
us_data = f_us.read()

f_in = open(r"C:\Users\CaseyL\Desktop\pylearn\stageOne\23_可视化\lineChart\India.json", "r", encoding="UTF-8")
in_data = f_in.read()

f_jp = open(r"C:\Users\CaseyL\Desktop\pylearn\stageOne\23_可视化\lineChart\Japan.json", "r", encoding="UTF-8")
jp_data = f_jp.read()

# json转为python字典
us_dict = json.loads(us_data)
in_dict = json.loads(in_data)
jp_dict = json.loads(jp_data)

us_trend_data = us_dict["data"][0]["trend"]
us_y_data = us_trend_data["list"][0]["data"][:314]

in_trend_data = in_dict["data"][0]["trend"]
in_y_data = in_trend_data["list"][0]["data"][:314]

jp_trend_data = jp_dict["data"][0]["trend"]
jp_y_data = jp_trend_data["list"][0]["data"][:314]

# 构建折线图对象
line = Line(
    init_opts=InitOpts(width="2200px", height="1200px", page_title="2022中美日新冠疫情确诊人数", theme=ThemeType.ESSOS)
)
# 添加x轴数据 x轴是公用，所以使用一个国家的数据即可
us_x_data = us_trend_data["updateDate"][:314]
line.add_xaxis(us_x_data)

# 添加y轴数据
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=True))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=True))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=True))

# 配置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="2022中美日新冠疫情确诊人数", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 120000},
            {"value": 100000, "label": '100000（自定义特殊颜色）', "color": 'grey'},
            {"min": 90000, "max": 120000},
            {"min": 50000, "max": 90000},
            {"min": 20000, "max": 50000},
            {"min": 10000, "max": 20000},
            {"min": 5000, "max": 10000},
            {"min": 1000, "max": 5000},
            {"min": 500, "max": 1000},
            {"max": 500}]
        ),
    datazoom_opts=DataZoomOpts(is_show=True),

)


# 生成图表
line.render()

f_us.close()
f_in.close()
f_jp.close()



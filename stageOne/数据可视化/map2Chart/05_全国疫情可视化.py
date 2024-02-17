import json

from pyecharts.charts import Map
from pyecharts.globals import ThemeType
from pyecharts.options import *

f = open(r"C:\Users\CaseyL\Desktop\pylearn\stageOne\23_可视化\map2Chart\covid.json", "r", encoding="UTF-8")
data = f.read()
f.close()

data_dict = json.loads(data)
province_data_list = data_dict["areaTree"][0]["children"]
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]
    province_confirm = province_data["total"]["confirm"]
    if province_name == '上海':
        province_name = province_name + '市'
    elif province_name == '香港':
        province_name = province_name + '特别行政区'
    elif province_name == '北京':
        province_name = province_name + '市'
    elif province_name == '天津':
        province_name = province_name + '市'
    elif province_name == '广西':
        province_name = province_name + '壮族自治区'
    elif province_name == '重庆':
        province_name = province_name + '市'
    elif province_name == '澳门':
        province_name = province_name + '特别行政区'
    elif province_name == '内蒙古':
        province_name = province_name + '自治区'
    elif province_name == '西藏':
        province_name = province_name + '自治区'
    elif province_name == '宁夏':
        province_name = province_name + '回族自治区'
    elif province_name == '新疆':
        province_name = province_name + '维吾尔自治区'
    else:
        province_name = province_name + '省'
    data_list.append((province_name, province_confirm))

print(data_list)

map = Map(
    init_opts=InitOpts(width="2200px", height="1200px", page_title="全国疫情地图", theme=ThemeType.ESSOS)
)
map.add("各省确诊人数", data_list, "china")
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"max": 9},
            {"min": 10, "max": 99},
            {"min": 100, "max": 499},
            {"min": 500, "max": 999},
            {"min": 1000, "max": 1999},
            {"min": 2000, "max": 4999},
            {"min": 5000, "max": 99999},
            {"min": 10000},
        ]
    )
)

map.render("全国疫情地图.html")

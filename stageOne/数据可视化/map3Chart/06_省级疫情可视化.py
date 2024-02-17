import json

from pyecharts.charts import Map
from pyecharts.globals import ThemeType
from pyecharts.options import *

f = open(r"C:\Users\CaseyL\Desktop\pylearn\stageOne\23_可视化\map2Chart\covid.json", "r", encoding="UTF-8")
data = f.read()
f.close()

data_dict = json.loads(data)
gd_data_list = data_dict["areaTree"][0]["children"][7]["children"]
data_list = []
for city_data in gd_data_list:
    city_name = city_data["name"]
    city_confirm = city_data["total"]["confirm"]
    data_list.append((city_name + '市', city_confirm))

print(data_list)

map = Map(
    init_opts=InitOpts(width="2200px", height="1200px", page_title="广东省疫情地图", theme=ThemeType.ESSOS)
)
map.add("广东省确诊人数", data_list, "广东")
map.set_global_opts(
    title_opts=TitleOpts(title="广东省确诊人数", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

map.render("广东省疫情地图.html")

from pyecharts.charts import Map
from pyecharts.globals import ThemeType
from pyecharts.options import *

map = Map(
    init_opts=InitOpts(width="2200px", height="1200px", page_title="测试地图", theme=ThemeType.ESSOS)
)

data = [
    ("北京市", 99),
    ("广东省", 499),
    ("上海市", 10000),
    ("西藏自治区", 10000),
    ("新疆维吾尔自治区", 9),
    ("内蒙古自治区", 59),
    ("四川省", 764),
    ("江苏省", 1000),
    ("江西省", 232),
    ("湖南省", 1000),
    ("浙江省", 653),
    ("陕西省", 120000),
    ("黑龙江省", 1200000)

]
map.add("测试地图", data, "china")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9人"},
            {"min": 10, "max": 99, "label": "10-99人"},
            {"min": 100, "max": 999, "label": "100-999人"},
            {"min": 1000, "max": 9999, "label": "1000-9999人"},
            {"min": 10000, "max": 99999, "label": "10000-9999人"},
            {"min": 100000, "max": 999999, "label": "10000-9999人"},
            {"min": 1000000, "max": 9999999, "label": "10000-9999人"},
        ]
    )
)


map.render()
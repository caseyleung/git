"""
pyecharts模块
"""
from pyecharts.charts import *
from pyecharts.globals import ThemeType
from pyecharts.options import *

# 创建一个折线图对象
line = Line(
    init_opts=InitOpts(width="1400px", height="800px", page_title="商品销量折线图", theme=ThemeType.LIGHT)
)
# x_data = ["中国", "USA", "UK"]
# y_data = [30, 20, 15]
# y_data = [30, 20, 15]
x_data = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
y_data = [5, 20, 36, 10, 75, 90]
# 给折线图x，y轴添加数据
line.add_xaxis(x_data)
line.add_yaxis("商家A", y_data)

# 配置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="商品销量", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

line.render()
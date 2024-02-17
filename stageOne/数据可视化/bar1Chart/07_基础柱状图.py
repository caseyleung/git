from pyecharts.charts import Bar
from pyecharts.globals import *
from pyecharts.options import *

bar = Bar(
    init_opts=InitOpts(width="2200px", height="1200px", page_title="基础柱状图", theme=ThemeType.ESSOS)
)

bar.add_xaxis(["中国", "美国", "英国"])
bar.add_yaxis("GDP", [20, 30, 10], label_opts=LabelOpts(position="right"))

bar.reversal_axis()

bar.render("基础柱状图.html")
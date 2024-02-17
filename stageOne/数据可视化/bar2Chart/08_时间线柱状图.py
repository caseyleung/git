from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import *

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP",[20, 30, 10], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar( )
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP",[50, 40, 30], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP",[80, 60, 140], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

timeline = Timeline(
    init_opts=InitOpts(width="2200px", height="1200px", page_title="基础柱状图", theme=ThemeType.ESSOS)
)

timeline.add(bar1, "2021年GDP")
timeline.add(bar2, "2022年GDP")
timeline.add(bar3, "2023年GDP")

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

timeline.render("基础柱状图-时间线.html")
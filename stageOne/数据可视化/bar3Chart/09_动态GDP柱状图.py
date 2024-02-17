"""
拓展列表的sort方法
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import InitOpts, LabelOpts, TitleOpts

# my_list = [["a", 33], ["b", 55], ["c", 11]]
#
# # def choose_sort_key(element):
# #     return element[1]
# #
# #
# # my_list.sort(key=choose_sort_key, reverse=True)
# my_list.sort(key=lambda element:element[1], reverse=True)
# print(my_list)

f = open(r"C:\Users\CaseyL\Desktop\pylearn\stageOne\23_可视化\bar3Chart\1960-2019全球GDP数据.csv", "r", encoding="GBK")

data_lines = f.readlines()
data_lines.pop(0)

data_dict = {}
# { year：[[country, gdp], [country, gdp],....], year：[[country, gdp], [country, gdp],....], .......}
for line in data_lines:
    str_line = line.split(',')
    year = int(str_line[0])
    country = str_line[1]
    gdp = float(str_line[2])
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# print(data_dict)

# 排序年份
sorted_list_key = sorted(data_dict.keys())

# print(sorted_list_key)
print(sorted_list_key[2])
print(data_dict[sorted_list_key[2]])
timeline = Timeline(
    init_opts=InitOpts(width="2200px", height="1200px", page_title="基础柱状图", theme=ThemeType.ESSOS)
)

for year in sorted_list_key:
    data_dict[year].sort(key=lambda element:element[1], reverse=True)
    top_year_data = data_dict[year][0:8]
    x_data = []  # 国家
    y_data = []  # gdp数据
    for country_gdp in top_year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1] / 100000000)

    # 构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )

    timeline.add(bar, str(year))


timeline.add_schema(
    play_interval=400,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

timeline.render("1960-2019全球前八GDP数据.html")


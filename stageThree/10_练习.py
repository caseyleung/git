import json

from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = r"C:\Program Files\Python39\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.textFile(r"C:\Users\CaseyL\Desktop\pylearn\stageThree\orders.txt")
# todo 需求一： 城市销售额排名
# 取出json字符串
rdd_split = rdd.flatMap(lambda item: item.split("|"))
# 将json字符串转化为字典
dict_rdd = rdd_split.map(lambda x: json.loads(x))
# 取出城市和销售额数据
# (城市，销售额)
dict_city_rdd = dict_rdd.map(lambda x: (x['areaName'], int(x['money'])))
# 按照城市分组
city_result_rdd_sort_by = dict_city_rdd.reduceByKey(lambda a, b: a + b).sortBy(lambda x: x[1], ascending=False, numPartitions=1)


# todo 需求二： 全部城市有哪些商品类别在售卖
category_rdd = dict_rdd.map(lambda x: x['category']).distinct()

# todo 需求三： 北京市有哪些商品类别在售卖
beijing_data_rdd = dict_rdd.filter(lambda x: x['areaName'] == '杭州')
beijing_dat_result_rdd = beijing_data_rdd.map(lambda x: x['category']).distinct()

print(rdd.collect())
print(rdd_split.collect())
print(dict_rdd.collect())
print(dict_city_rdd.collect())
print(city_result_rdd_sort_by.collect())
print(category_rdd.collect())
print(beijing_data_rdd.collect())
print(beijing_dat_result_rdd.collect())


sc.stop()

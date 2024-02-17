from pyspark import SparkConf, SparkContext

# 找到python的解释器
import os

os.environ['PYSPARK_PYTHON'] = r"C:\Program Files\Python39\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])  # list

# 通过map方法将全部数据乘以10
# def func(data):
#     return data * 10
# rdd2 = rdd.map(func)

rdd2 = rdd.map(lambda x: x * 100 + 5).map(lambda x: x + 10)
print(rdd2.collect())

sc.stop()

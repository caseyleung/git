"""
功能：针对KV型RDD，自动按照key分组，然后根据你提供的聚合逻辑，完成组内数据（value)的聚合操作
如：
rdd.reduceKey(func)
func：(v, v) -> v
接受2个传入参数(类型要一致), 返回一个返回值, 类型和传入要求一致

按照k分组，再计算v
"""

from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = r"C:\Program Files\Python39\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

test_data = [('male', 99), ('male', 88), ('female', 99), ('female', 66)]
rdd = sc.parallelize(test_data)

rdd1 = rdd.reduceByKey(lambda x, y: x + y)
print(rdd1.collect())

sc.stop()

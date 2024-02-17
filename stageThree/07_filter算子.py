from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = r"C:\Program Files\Python39\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])  # list
rdd1 = rdd.filter(lambda num: num % 2 == 0)

print(rdd1.collect())

sc.stop()



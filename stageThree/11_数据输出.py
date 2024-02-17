"""
collect: 将RDD内容转换为list
reduce: 对RDD内容进行自定义聚合
take: 取出RDD的前N个元素组成list
count: 统计RDD元素个数
"""

from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = r"C:\Program Files\Python39\python.exe"
os.environ['HADOOP_PYTHON'] = r"E:\hadoop-3.3.5"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])

# collect算子，输出RDD为list对象
rdd_list: list = rdd.collect()
print(rdd_list)
print(type(rdd_list))

# reduce算子，对RDD进行两两聚合
num = rdd.reduce(lambda a, b: a + b)
print(num)

# take算子，取出RDD前N个元素
take_list = rdd.take(3)
print(take_list)

# count, 统计RDD内有多少条数据，返回值为数字
num_count = rdd.count()
print(num_count)


rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = sc.parallelize([("hello", 3), ("spark", 5), ("hi", 7)])
rdd3 = sc.parallelize([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

rdd1.saveAsTextFile(r"C:\Users\CaseyL\Desktop\pylearn\stageThree\rdd1")
rdd2.saveAsTextFile(r"C:\Users\CaseyL\Desktop\pylearn\stageThree\rdd2")
rdd3.saveAsTextFile(r"C:\Users\CaseyL\Desktop\pylearn\stageThree\rdd3")


sc.stop()






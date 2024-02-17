"""
功能：对rdd执行map操作，然后进行解除嵌套操作
如：
lst = [[1,2,3], [4,5,6], [7,8,9]]
lst = [1,2,3,4,5,6,7,8,9]
"""

from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = r"C:\Program Files\Python39\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize(["hello spongebob", ", i'm learning python", ". how are you, patrick star"])

rdd2 = rdd.map(lambda x: x.split(" "))
rdd3 = rdd.flatMap(lambda x: x.split(" "))
print(rdd2.collect())
print(rdd3.collect())



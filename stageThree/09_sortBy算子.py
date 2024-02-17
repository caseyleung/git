"""
rdd.sortBy(func, ascending=False, numPartitions=1)
func: 对那个数据进行排序
ascending=False: true -> asc,  false -> false
numPartitions=1: 涉及到分布式的理论
"""

from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = r"C:\Program Files\Python39\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.textFile(r"C:\Users\CaseyL\Desktop\pylearn\stageThree\hello.txt")

word_rdd = rdd.flatMap(lambda x: x.split(" "))
word_rdd1 = word_rdd.map(lambda word: (word, 1))
# 分组求和
word_rdd2 = word_rdd1.reduceByKey(lambda a, b: a + b)

# 对结果集进行排序
word_rdd2_sort = word_rdd2.sortBy(lambda x: x[1], ascending=False, numPartitions=1)


print(word_rdd2_sort.collect())










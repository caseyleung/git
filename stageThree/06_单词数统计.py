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


print(word_rdd2.collect())

sc.stop()





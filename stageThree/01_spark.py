"""
pyspark的执行环境入口对象是：类SparkContext的类对象

SparkContext类对象，是PySpark编程中一切功能的入口
PySpark的编程，主要分为以下三大步骤：
        数据输入           ----->             数据处理计算            ----->      数据输出
通过SparkContext类对象的成员方法          通过RDD类对象的成员方法                将处理完成后的RDD对象
完成数据的读取操作                        完成各种数据计算的需求                 调用各种成员方法完成
读取后得到RDD类对象                                                         写出文件，转换为list等操作
"""

from pyspark import SparkConf, SparkContext

# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 基于SparkConf类对象创建SparkContext类对象
sc = SparkContext(conf=conf)

print(sc.version)

sc.stop()

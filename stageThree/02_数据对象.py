from pyspark import SparkConf, SparkContext
# 最好把java，scala，hadoop，spark，都装配一遍，hadoop要用pyspark匹配的版本
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 1.通过parallelize方法将python对象加载到Spark内，成为RDD对象(resilient distributed dataset, 分布式弹性数据集， 是pyspark中数据计算的载体)
# 它可以提供 1.数据存储  2.数据计算的各类方法  3.数据计算的方法，返回值依旧是RDD
rdd1 = sc.parallelize([1, 2, 3, 4, 5])  # list
rdd2 = sc.parallelize((1, 2, 3, 4, 5))  # tuple
rdd3 = sc.parallelize("abcdefg")  # list
rdd4 = sc.parallelize({1, 2, 3, 4, 5})  # set
rdd5 = sc.parallelize({"name": "zhangsan", "age": 33})  # dict

# 如果查看RDD里面有什么内容，需要用collect()
print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())

# 2.读取文件转为RDD对象
# rdd = sc.textFile("文件路径")
rdd = sc.textFile(r"C:\Users\CaseyL\Desktop\pylearn\stageThree\hello.txt")
print(rdd.collect())

sc.stop()


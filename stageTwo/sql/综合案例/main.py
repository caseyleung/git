
"""
面向对象，数据分析案例，主业务逻辑代码
实现步骤：
1.设计一个类，可以完成数据的封装
2.设计一个抽象类，定义文件读取相关功能，并使用子类实现具体功能
3.读取文件，生成数据对象
4.进行数据需求的逻辑计算
5.通过pyecharts进行图形绘制
"""
from pymysql import Connection
from file_define import TextFileReader, JsonFileReader
from data_define import Record

cvs_file_reader = TextFileReader(r"C:\Users\CaseyL\Desktop\pylearn\stageTwo\数据分析案例\2011年1月销售数据.cvs")
json_file_reader = JsonFileReader(r"C:\Users\CaseyL\Desktop\pylearn\stageTwo\数据分析案例\2011年2月销售数据.json")

jan_data: list[Record] = cvs_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

all_data: list[Record] = jan_data + feb_data

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="",
    autocommit=True
)

cursor = conn.cursor()
conn.select_db("pylearn")

for record in all_data:
    sql = f"insert into orders(date, order_id, money, province) " \
          f"values('{record.date}', '{record.order_id}', {record.money}, '{record.province}')"
    print(sql)
    # cursor.execute(sql)


conn.close()




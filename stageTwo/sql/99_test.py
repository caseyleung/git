import json

from pymysql import Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="",
    autocommit=True
)

print(conn.get_server_info())
print(conn.get_host_info())

cursor = conn.cursor()
conn.select_db("pylearn")

cursor.execute("select * from orders")
results = cursor.fetchall()
data_list = []

for item in results:
    data_dict = {"date": str(item[0]), "order_id": item[1], "money": item[2], "province": item[3]}
    data_list.append(data_dict)


data_list = json.dumps(data_list, ensure_ascii=False)
data_str = data_list.replace("}, ", "}\n")
data_str = data_str[1:len(data_str)-1]
# print(data_str)

f = open(r"C:\Users\CaseyL\Desktop\pylearn\stageTwo\sql\数据还原.txt", "a", encoding="UTF-8")
f.write(data_str)
f.close()


conn.close()
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

conn.select_db("st")

cursor.execute("select * from student")
results = cursor.fetchall()
for item in results:
    print(item)

# cursor.execute("insert into student values('202211113', '林军杰', '男', 38, 'ART')")
# conn.commit()

conn.close()

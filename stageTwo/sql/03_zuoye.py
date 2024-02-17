"""
将数据库的数据读出来写入到文件中
["date": "2011-02-27", "order_id": "494158aa-2fc2-4223-9ad6-b54e642f3d6f", "money": 2746, "province": "广东省"]

(datetime.date(2011, 2, 25), 'c8621d70-9987-44d8-9380-47c75a298c5b', 1515, '广东省')
"""
import datetime

# print(datetime.date(2011, 2, 25))


# 1. 将数据从数据库里面读出来 -> list
# 2. 封装成 dict 格式
# 3. 写入到文件中
data_list =(datetime.date(2011, 2, 25), 'c8621d70-9987-44d8-9380-47c75a298c5b', 1515, '广东省')
print(data_list)


# print(data_list[0])
# data_dict = {}
# # data_dict["date"] = datetime.date(data_list[0])
# data_dict["date"] = data_list[0]
# data_dict["order_id"] = data_list[1]
# data_dict["money"] = data_list[2]
# data_dict["province"] = data_list[3]

# print(data_dict)


# 封装成 dict 格式    key: value
# 一个个字典写入到文件（这样的话消耗很大）
# 一个个字段添加到list中， 最后去掉[]就可以了





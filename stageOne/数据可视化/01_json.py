"""
pyton数据和json数据的相互转化
"""
import json

# 符合json格式的python数据
data = [{"name":"jack", "age":43}, {"name":"tim", "age":23}, {"name":"王大锤", "age":23}]
print(f"data的数据类型: {type(data)}, 数据内容: {data}")

# 通过json.dumps(data)方法把python数据转为json数据   ensure_ascii
data = json.dumps(data, ensure_ascii=False)
print(f"data的数据类型: {type(data)}, 数据内容: {data}")

# 通过json.loads(data)方法把json数据转化为python数据  strict
data = json.loads(data)
print(f"data的数据类型: {type(data)}, 数据内容: {data}")


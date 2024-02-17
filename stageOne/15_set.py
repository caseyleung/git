# 定义集合set：1.不能重复；2.无序
my_set = {"c++", "python", "go", "c#", "python", "go", "c#"}
my_set_empty = set()

print(f"my_set的内容是：{my_set}, 类型是：{type(my_set)}")
print(f"my_set_empty的内容是：{my_set_empty}, 类型是：{type(my_set_empty)}")

# 添加新元素
my_set.add("lua")
my_set.add("js")
print(f"my_set添加后结果是：{my_set}")

# 移除元素
my_set.remove("go")
print(f"my_set移除go，结果是：{my_set}")

# 随机取出元素
element = my_set.pop()
print(f"集合被随机取出来的元素是：{element}")

# 清空集合，clear
# my_set.clear()


# 取两个集合的差集
my_set2 = {"c++", "c", "c#"}
set3 = my_set.difference(my_set2)
print(f"取两个集合的差集:{set3}")
print(my_set)
print(my_set2)

# 消除两个集合的差集
set4 = my_set.difference_update(my_set2)
print(f"消除差集后，集合my_set的结果:{my_set}")
print(f"消除差集后，集合my_set2的结果:{my_set2}")

# 两个集合合并 union
set5 = my_set.union(my_set2)
print(f"两个集合合并后：{set5}")

# 统计集合元素数量
num = len(set5)
print(f"集合set5的数量是：{len(num)}")

# 集合遍历
# while or for




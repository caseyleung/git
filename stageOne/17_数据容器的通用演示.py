"""
演示数据容器的通用功能
"""

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3}

# len元素个数
print(f"列表的元素个数有：{len(my_list)}")
print(f"元组的元素个数有：{len(my_tuple)}")
print(f"字符串的元素个数有：{len(my_str)}")
print(f"集合的元素个数有：{len(my_set)}")
print(f"字典的元素个数有：{len(my_dict)}")

print()
# max最大元素
print(f"列表中最大的元素：{max(my_list)}")
print(f"元组中最大的元素：{max(my_tuple)}")
print(f"字符串中最大的元素：{max(my_str)}")
print(f"集合中最大的元素：{max(my_set)}")
print(f"字典中最大的元素：{max(my_dict)}")

print()
# min最小元素
print(f"列表中最小的元素：{min(my_list)}")
print(f"元组中最小的元素：{min(my_tuple)}")
print(f"字符串中最小的元素：{min(my_str)}")
print(f"集合中最小的元素：{min(my_set)}")
print(f"字典中最小的元素：{min(my_dict)}")

print()
print(my_list)
print(my_tuple)
print(my_str)
print(my_set)
print(my_dict)

print()
# 类型转换
# 容器 --> 列表
print(f"列表 --> 列表：{list(my_list)}")
print(f"元组 --> 列表：{list(my_tuple)}")
print(f"字符串 --> 列表：{list(my_str)}")
print(f"集合 --> 列表：{list(my_set)}")
print(f"字典 --> 列表：{list(my_dict)}")

print()
# 容器 --> 元组
print(f"列表 --> 元组：{tuple(my_list)}")
print(f"元组 --> 元组：{tuple(my_tuple)}")
print(f"字符串 --> 元组：{tuple(my_str)}")
print(f"集合 --> 元组：{tuple(my_set)}")
print(f"字典 --> 元组：{tuple(my_dict)}")

print()
# 容器 --> 字符串
print(f"列表 --> 字符串：{str(my_list)}")
print(f"元组 --> 字符串：{str(my_tuple)}")
print(f"字符串 --> 字符串：{str(my_str)}")
print(f"集合 --> 字符串：{str(my_set)}")
print(f"字典 --> 字符串：{str(my_dict)}")

print()
# 容器 --> 集合
print(f"列表 --> 集合：{set(my_list)}")
print(f"元组 --> 集合：{set(my_tuple)}")
print(f"字符串 --> 集合：{set(my_str)}")
print(f"集合 --> 集合：{set(my_set)}")
print(f"字典 --> 集合：{set(my_dict)}")

print()
# 容器 --> 字典
# print(f"列表 --> 字典：{dict(my_list)}")
# print(f"元组 --> 字典：{dict(my_tuple)}")
# print(f"字符串 --> 字典：{dict(my_str)}")
# print(f"集合 --> 字典：{dict(my_set)}")
print(f"字典 --> 字典：{dict(my_dict)}")


my_list = [2, 4, 5, 1, 3]
my_tuple = (4, 2, 3, 1, 5)
my_str = "defgabc"
my_set = {4, 2, 3, 1, 5}
my_dict = {"key3": 1, "key2": 2, "key1": 3}

print()
print("---------------")
print("sorted排序---放在列表中")
print(f"列表对象的排序结果：{sorted(my_list)}")
print(f"元组对象的排序结果：{sorted(my_tuple)}")
print(f"字符串对象的排序结果：{sorted(my_str)}")
print(f"集合对象的排序结果：{sorted(my_set)}")
print(f"字典对象的排序结果：{sorted(my_dict)}")

print()
# 反向排序
print(f"列表对象的排序结果：{sorted(my_list, reverse=True)}")

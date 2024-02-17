"""
列表：[]
元组：()           set(), dict(), tuple()
字符串：""
集合: {}
"""

# 定义字典
my_dict1 = {"王力鸿": 99, "周杰轮": 88, '林俊节': 77, "泰森": 101}
#
my_dict2 = {}
my_dict3 = dict()
print(f"字典1的内容：{my_dict1}, 类型：{type(my_dict1)}")
print(f"字典2的内容：{my_dict2}, 类型：{type(my_dict2)}")
print(f"字典3的内容：{my_dict3}, 类型：{type(my_dict3)}")

# 定义重复key的字典
my_dict1 = {"王力鸿": 99, "王力鸿": 90, "周杰轮": 88, '林俊节': 77, "泰森": 101}
print(f"字典1的内容：{my_dict1}, 类型：{type(my_dict1)}")

# 从字典中基于key获取value
score = my_dict1["王力鸿"]
print(f"王力鸿的考试分数是：{score}")
score = my_dict1["周杰轮"]
print(f"周杰轮的考试分数是：{score}")

stu_score_dict = {
    "王力鸿": {
        "语文": 87,
        "数学": 74,
        "英语": 94
    },
    "周杰轮": {
        "语文": 72,
        "数学": 21,
        "英语": 32
    },
    "林俊节": {
        "语文": 77,
        "数学": 34,
        "英语": 91
    }
}
print(f"学生考试的成绩信息是：{stu_score_dict}")
score = stu_score_dict["周杰轮"]["数学"]
print(f"周杰轮的语文分数是：{score}")

# 新增元素
my_dict1["张学油"] = 666
print(f"元素经过新增后，结果是：{my_dict1}")

# 更新元素
my_dict1["周杰轮"] = 33

# 删除元素
score = my_dict1.pop("周杰轮")
print(f"从字典中一个元素，结果是：{my_dict1}， 分数是：{score}")

# 清空元素
# my_dict1.clear()

# 获取全部的key
keys = my_dict1.keys()
print(f"字典的全部keys是：{keys}")

# 遍历字典
# for循环
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict1[key]}")


# 统计字典内的元素数量
num = len(my_dict1)
print(f"字典的元素数量：{num}")

my_str = "this is spongebob"

# 通过下标索引取值
v1 = my_str[2]
v2 = my_str[-4]
print(f"从字符串{my_str}取下标为的元素，值是：{v1}, 取下标为-4的元素。值是：{v2}")

# index方法
v3 = my_str.index("is")
print(f"在字符串{my_str}中查找，其起始下标是：{v3}")

# replace方法
new_my_str = my_str.replace("is", "are")
print(f"将字符串{my_str}，进行替换后{new_my_str}")

# split方法
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}，进行替换后得到：{my_str_list}，类型是：{type(my_str_list)}")

# stripe方法
new_str = "   hello, patrick   "
print(f"字符串被{new_str}被strip()后，结果是{new_str.strip()}")
new_str = "11111hello, patrick11111"
print(f"字符串被{new_str}被strip('111)后，结果是{new_str.strip('1')}")
print(f"字符串被{new_str}被strip('111)后，结果是{new_str.strip('111')}")

print(f"字符串{my_str}的长度是：{len(my_str)}")

index = 0
while index < len(my_str):
    print(my_str[index])
    index += 1

print()
for i in my_str:
    print(i)


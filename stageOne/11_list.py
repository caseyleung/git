name_list = ['hi','c++', 'python']
print(name_list)
print(type(name_list))

ran_list = ['list', 666, True]
print(ran_list)
print(type(ran_list))

my_list = [[1,2,3], True, [4,5,6]]
print(my_list)
print(type(my_list))

print(my_list[0])
print(my_list[0][0])
print(my_list[0][1])
print(my_list[1])
print(my_list[2])
print(my_list[-2])

# index方法
index = name_list.index('python')
print(f"python在列表中的下标索引是{index}")

# 修改元素
name_list[0] = 'go'
print(f"列表被修改后，结果是{name_list}")

# 插入元素
# 指定下标位置的
name_list.insert(1, 'lua')
print(f"列表插入元素后，结果是{name_list}")

# 在尾部追加
name_list.append('rust')
print(f"列表在追加元素后，结果是{name_list}")

# 追加一批元素
name_list.append(my_list)
print(f"列表在追加了一批元素后，结果是{name_list}")

name_list.extend(ran_list)
print(f"列表在追加了一批元素后，结果是{name_list}")


# 删除元素
# 方式1
del name_list[5]
print(f"列表删除后结果是{name_list}")

# 方式2
name_list.pop(0)
print(f'列表删除后结果是：{name_list}')


# 删除元素、清空列表
name_list.insert(1,'go')
name_list.insert(1,'go')
print(f'添加元素后的结果是: {name_list}')

name_list.remove('go')
print(f'通过remove方法移除元素后，列表的结果是；{name_list}')

# 统计元素
count = name_list.count('go')
list_len = len(name_list)
print(f"列表中的\"go\"元素个数：{count}")
print(f"列表中的元素个数：{list_len}")

# 清空列表
# name_list.clear()
# print(f"列表被清空后：{name_list}")




# 遍历
# while循环
index = 0
while index < len(name_list):
    element = name_list[index]
    print(f"列表的元素是：{element}")
    index += 1
print()
# for循环
for i in name_list:
    print(f"列表的元素是：{i}")

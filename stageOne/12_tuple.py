t1 = (1, "Hello", True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)}, 内容是: {t1}")
print(f"t2的类型是：{type(t2)}, 内容是: {t2}")
print(f"t3的类型是：{type(t3)}, 内容是: {t3}")

# 单个元素的元组
t4 = ("hello")
t5 = ("hello", )
print(f"t4的类型是：{type(t4)}, 内容是: {t4}")
print(f"t5的类型是：{type(t5)}, 内容是: {t5}")

# 元组嵌套
t6 = ((1, "tuple", True), (1,"turbo", False))
print(f"t6的类型是：{type(t6)}, 内容是: {t6}")

# 下标索引
print(t6[1][1])
print(t6[0][1])

# 操作
# print(t6.index("turbo"))
# print(t6.index(True))

t7 = ("c++", "go", "", "python", "java", "rust", "go")
print(t7.index("go"))
print(t7.index(""))
print(t7.count("go"))
print(t7.count(""))
print(len(t7))

# 遍历: while
index = 0
while index < len(t7):
    print(f"t7元组的元素有：{t7[index]}")
    index += 1


print()
# 遍历：for
for element in t7:
    print(f"t7元组的元素有：{element}", end=" ")


print()
# 元组里面的元素
t8 = (1, 2, ["apple", "banana"])
print(f"t8的内容是: {t8}")
t8[2][0] = "cherry"
t8[2][1] = "pearl"
print(f"t8的内容是：{t8}")
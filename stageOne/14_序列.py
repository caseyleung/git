"""
序列[起始下标：结束下标：步长]
"""

my_list = [0,1,2,3,4,5,6]
result1 = my_list[1:4]
print(f"结果是：{result1}")

my_tuple = (0,1,2,3,4,5,6)
result2 = my_tuple[:]
print(f"结果是：{result2}")

my_str = "0123456"
result3 = my_str[::2]
print(f"结果是：{result3}")

# 步长为负数 (从尾到头)
result4 = my_str[::-1] # 等同将序列反转
print(f"结果是：{result4}")

result5 = my_str[3:1:-1]
print(f"结果是：{result5}")

result6 = my_str[::-2]
print(f"结果是：{result6}")
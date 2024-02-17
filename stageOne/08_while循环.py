
# i = 0
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1
# print(sum)
# print(f"1到100的和是 {sum}")

"""
演示while循环的基础案列 - 猜数字
"""

# import random
# num = random.randint(1,100)
# count = 0
#
# flag = True
# while flag:
#     guess_num = int(input("请输入你猜的数字(1-100)："))
#     count += 1
#     if guess_num == num:
#         print("猜中了")
#         flag = False
#     else:
#         if guess_num > num:
#             print("猜大了")
#         else:
#             print("猜小了")
# print(f"你总共测算了{count}次")

i = 1
while i <= 9:
    j = 1
    while j <= 9:
        if i >= j:
            print(f"{i}*{j}={i*j}", end="  ")
            j += 1
        else:
            j += 1
    i += 1
    print()
print("done")












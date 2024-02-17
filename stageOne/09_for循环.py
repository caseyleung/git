
# name = "itheima is a brand of itcast"
# count = 0
# letter = "a"
#
# for i in name:
#     if i == letter:
#         count += 1
# print(f"{name}中共有：{count}个字母a")

x = 0
for x in range(10):
    print(x, end=" ")
print()

for x in range(4,10):
    print(x, end=" ")
print()

for x in range(4,10,2):
    print(x, end=" ")
print()

for x in range(10):
    print("111")
print()
# print(x

for i in range(1,10):
    j = 1
    for j in range(1,10):
        if i >= j:
            print(f"{i}*{j}={i*j}", end="  ")
    print()

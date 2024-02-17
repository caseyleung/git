"""
__init()__， 构造方法

在创建类对象的时候，会自动执行
在创建类对象的时候，将传入参数自动传递给__init__方法使用
"""


class Student:
    # name = None
    # age = None
    # tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print(f"student类创建了一个类对象")


# stu = Student("jack", 33, "1383883838")
# print(stu.name)
# print(stu.age)
# print(stu.tel)

stu = Student("casey", 24, "1393939339")
print(stu.name)
print(stu.age)
print(stu.tel)

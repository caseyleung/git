"""
__init__()构造方法，是python类内置的方法之一  ***注意不是int(), 而是init()
这些内置方法我们称之为：魔术方法
字符串方法：__str__   不写的话，输出内存地址
小于比较：__lt__
小于等于：__le__
等于比较：__eq__


"""


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


pp = person("jack", 43)
# print(pp)
# print(str(pp))


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"student类对象：name: {self.name}, age: {self.age}"

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age


stu = Student("casey0000", 24)
stu1 = Student("bond007", 33)

print(stu > stu1)
print(stu < stu1)
print(stu <= stu1)
print(stu == stu1)
# print(pp < stu1) # TypeError: '<' not supported between instances of 'person' and 'Student'


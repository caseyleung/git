"""
class name:
    类的属性：成员变量
    类的行为：成员方法

创建类对象的语法


如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头
但是，Python并没有从语法上严格保证私有属性或方法的私密性，
它只是给私有的属性和方法换了一个名字来妨碍对它们的访问，
事实上如果你知道更换名字的规则仍然可以访问到它们
"""


class Student:
    def __int__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

    def say_hi(self):
        print(f"大家好，我是{self.name}, 来自{self.native_place}, 请大家多多关照")

    def say_h1(self, msg):
        print(f"大家好，我是{self.name}, {msg}")


stu1 = Student()
stu1.name = "jack"
stu1.gender = "male"
stu1.nationality = "china"
stu1.native_place = "guangdong"
stu1.age = 33

print(stu1.name)
stu1.say_hi()
stu1.say_h1("喜欢篮球，练习时长两年半")

print(stu1)
print(str(stu1))


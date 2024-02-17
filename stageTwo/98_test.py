class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"student类对象：name: {self.name}, age: {self.age}"


stu = Student("casey", 24)
print(stu)
print(str(stu))
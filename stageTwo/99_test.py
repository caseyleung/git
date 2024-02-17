class Person:
    def __int__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name: {self.name}, age: {self.age}'


pp = Person("jackoo", 33)
print(pp)

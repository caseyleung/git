"""
演示多态

多态：同一个行为，使用不同的对象获得不同的状态
抽象类：包含抽象方法的类（没有具体的实现方法）

"""

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("wang, wangwang")

class Cat(Animal):
    def speak(self):
        print("meow, meow")


def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)





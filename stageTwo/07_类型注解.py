"""
类型注解：
-变量的类型注解
-函数形参和返回值的类型注解

类型注解仅仅是备注，不会影响程序的运行
"""
import json
import random

# 基础数据类型注解
# var_1: int = 10
# var_2: float = 3.1415926
# var_3: bool = True
# var_4: str = "10亿"

# 基础容器类型注解
# my_list: list = [1, 2, 3]
# my_tuple: tuple = (1, 2, 3)
# my_set: set = {1, 2, 3}
# my_dict: dict = {"jack": 33}
# my_str: str = "hhhhh"


# 容器类型详细注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str, bool] = (1, "2", True)
my_set: set[int] = {1, 2, 3}
my_dict: dict[str, int] = {"jack": 33}
my_str: str = "hhhhh"


# 类对象类型注解：
class Student:
    pass


# 类对象类型注解
stu: Student = Student()
# 在注释中进来类型注解
var_1 = random.randint(1, 10)  # type: int
var_2 = json.loads('{"name": "zhangsan"}')  # type: dict[str, str]


def func():
    return 10


var_3 = func()  # type: int

# 类型注解的限制
var_4: int = "hello"
var_5: str = 123

print(var_4)
print(var_5)


# 函数形参和返回值的类型注解
# 函数形参
def add(x: int, y: int):
    return x + y


add(1, 2)


# 返回值
def fun1(data: list) -> list:
    return data


fun1(my_list)

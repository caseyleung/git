""""
演示使用多个返回值
"""


def test_return():
    return 1, "hello", True


x, y, z = test_return()
print(x)
print(y)
print(z)

"""
演示多种传参的形式
"""


def user_info(name, age, gender):
    print(f"姓名是:{name}, 年龄是：{age}, 性别是:{gender}")


# 位置参数 - 默认使用形式
user_info('小明', 20, 'male')

print()
# 关键字参数
user_info(name='小王', age=11, gender='female')
user_info(age=11, gender='female', name='小绿')
user_info('甜甜', gender='female', age=11)


# 注意：默认值要在最后
def user_info(name, age, gender='男'):
    print(f"姓名是:{name}, 年龄是：{age}, 性别是:{gender}")


# 默认参数
print()
user_info(name='小王', age=11)
user_info(name='小王', age=11, gender='female')

print()


# 不定长 - 位置不定长，*号
# 不定长定义的形式参数会作为元组存在，接收不定长数量的参数传入
# 将args换作其他的可以吗
def usr_info(*aaaargs):
    print(f"args参数的类型是：{type(aaaargs)}, 内容是：{aaaargs}")


usr_info(1, 2, 3, 'jack', 'male', 'captain')


# 不定长 - 关键字不定长， **号。 形式是限定的， kv。
# 将kwargs换作其他的可以吗
def user_info(**kxxwargs):
    print(f"args参数的类型是：{type(kxxwargs)}, 内容是：{kxxwargs}")


user_info(age=11, gender='female', name='小绿')

"""
演示函数作为参数传递
"""
print()


# 定义一个函数，接收另一个函数作为传入参数
# 作用：传入计算逻辑，而非数据
def test_func(compute):
    result = compute(1, 3)
    print(f"compute参数的类型是：{type(compute)}, 计算结果是：{result}")


# 定义一个函数，准备作为参数传入另一个函数
def compute(x, y):
    return x + y


# 调用，并传入函数
test_func(compute)

"""
 演示lambda匿名函数
"""
print()


# 定义一个函数，接受其他函数输入
def test_func(compute):
    result = compute(1, 4)
    print(f"compute参数的类型是：{type(compute)}, 计算结果是：{result}")


# 通过lambda匿名函数的形式，将匿名函数作为参数传入
# lambda 传入参数：函数体（一行代码）
test_func(lambda x, y: x + y)

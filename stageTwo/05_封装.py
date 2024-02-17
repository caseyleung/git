"""
面向对象： 封装、继承、多态
基于模板去创建实体，使用对象完成功能开发


对用户隐藏的属性和行为。
类中提供了私有成员的形式支持。
-私有成员变量： 无法赋值，也无法获取值
-私有成员方法： 无法直接被类对象使用

定义私有成员的方式：
-私有成员变量：变量名以 __ 开头
-私有成员方法：方法名以 __ 开头
既可以完成私有成员变量
"""


class Phone:
    __current_voltage = 0

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话, 并且开启单核模式进行省电。")


phone = Phone()
# phone.__keep_single_core()  # AttributeError: 'Phone' object has no attribute '__keep_single_core'
# print(phone.__current_voltage)  # AttributeError: 'Phone' object has no attribute '__current_voltage'
phone.call_by_5g()

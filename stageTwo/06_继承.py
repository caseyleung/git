"""
继承分为：单继承和多继承
关键字： pass 补全语法



"""


# 演示单继承
class Phone:
    IMEI = None
    producer = "HH"

    def call_by_4g(self):
        print("4g通话")

    def call_by_5g(self):
        print("使用5g通话")


class Phone2022(Phone):
    face_id = "10001"

    def call_by_5g(self):
        print("2022年新功能，5g通话")


phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()

print()


# 演示多继承, 多个父类中，同名的成员， 默认继承的顺序（从左到右）优先级
class NPCReader:
    nfc_type = "5 generation"
    producer = "mmm"

    def read_card(self):
        print("nfc 读卡")

    def write_card(self):
        print("nfc 写卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")


class MyPhone(Phone, NPCReader, RemoteControl):
    # pass  # 补全语法
    producer = "x phone"

    def call_by_5g(self):
        print("开启CPU单核模式，确保通话的时候省点")
        # print("使用5g通话")
        # method1
        # print(f"父类的厂商: {Phone.producer}")
        # Phone.call_by_5g(self)

        # method 2
        print(f"父类的厂商: {super().producer}")
        super().call_by_5g()
        print("关闭CPU单核性能，确保性能")


my_phone = MyPhone()
my_phone.call_by_5g()
my_phone.read_card()
my_phone.control()
print(my_phone.producer)

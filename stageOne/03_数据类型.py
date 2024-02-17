# python3中有六个标准的数据类型：
# number、string、list、tuple、set、dictionary

# 不可变：number、string、tuple
# 可变：list、dictionary、set

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

3 * 8 

print("学python" + "写脚本")

## 字符串格式化 %表示占位，s表示占位的地方和类型
## 多个变量用括号括起来
msg = "hi, this is a %s, 111"
print(msg, 111)

name = "casey"
messge = "my name is %s" %name
print(messge)

class_num = 57
avg_salary = 16000
msgg = "第%s届学生, 平均工资%s" %(class_num, avg_salary)
print(msgg)







# 赋值
counter = 100
miles = 1000.0
name = "runoob"

print(counter)
print(miles)
print(name)


# 多个变量赋值
a = b = c = 1
a, b, c = 1, 2, "runoob"


# 标准数据类型
# Number      #（数字）
# String      #（字符串）
# List        #（列表）
# Tuple       #（元组）
# Set         #（集合）
# Dictionary  #（字典）

# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。


# Number（数字）  type() ：查询变量所指的对象类型
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

# isinstance来判断对象类型
a = 111
print(isinstance(a, int))

# isinstance与type区别
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
class A:
    pass

class B(A):
    pass

print(isinstance(A(),A))    #True
print(type(A()) == A)       #True
print(isinstance(B(),A))    #True
print(type(B()) == A)       #False

# del删除元素
my_list = [1,2,3]
my_dict = {"name":"lowman", "age":12}

del my_list[0]  #[0]指针位置
del my_dict["name"]
print(my_list)
print(my_dict)

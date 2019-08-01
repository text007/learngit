
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


# Python数据类型转换
'''
int(x [,base])          将x转换为一个整数
float(x)                将x转换到一个浮点数
complex(real [,imag])   创建一个复数
str(x)                  将对象 x 转换为字符串
repr(x)                 将对象 x 转换为表达式字符串
eval(str)               用来计算在字符串中的有效Python表达式,并返回一个对象
list(s)                 将序列 s 转换为一个列表
set(s)                  转换为可变集合
frozenset(s)            转换为不可变集合
chr(x)                  将一个整数转换为一个字符
ord(x)                  将一个字符转换为它的整数值
hex(x)                  将一个整数转换为一个十六进制字符串
oct(x)                  将一个整数转换为一个八进制字符串
'''

print(int(3.15))            #转换为整数
print(float(-10))           #转换为浮点数
print(complex(3.2 + -5))    #创建一个复数
print(str("3.33"))          #转换为字符串
print(repr("3.33"))         #转换为表达式字符串

aTuple = (123, 'Google', 'Runoob', 'Taobao')
list2 = list(aTuple)
print ("列表元素 : ", list2) #转换为列表

print(set('abcde'))         #转换为可变集合
print(frozenset(range(10))) #转换为不可变集合
print(chr(78))              #将整数转换为字符
print(ord('N'))             #将字符转换为整数
print(hex(255))             #转换为十六进制字符串
print(oct(255))             #转换为八进制字符串

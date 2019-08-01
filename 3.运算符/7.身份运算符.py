
# 身份运算符
'''
is      是判断两个标识符是不是引用自一个对象,x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
is not  是判断两个标识符是不是引用自不同对象,x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
'''

# id():用于获取对象内存地址
a = 20
b = 20

if (a is b):
    print('a == b ')
else:
    print('a != b')

if (id(a) == id(b)):
    print('a 和 b 内存地址相同')
else:
    print('a 和 b 内存地址不同')

# 修改变量 b 的值
b = 30
if (a is b):
    print('a == b ')
else:
    print('a != b')

if (a is not b):
    print('a != b ')
else:
    print('a == b')


# 参数
'''
必需参数
关键字参数
默认参数
不定长参数
'''
# 必需参数
# 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样
def h3(stre):
    print(stre)
    return

h3('1')
# h3()  # 必须传入一个参数,否则报错
print('---------------')

# 关键字参数
# 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值
def h4(name, age):
    print('姓名：', name)
    print('年龄：',age)
    return

h4(age = 50, name = 'test')
print('---------------')

# 默认参数
def h5(name, age = 35):
    print('姓名：', name)
    print('年龄：',age)
    return
h5(age = 50, name ='test')
print('---------------')
h5(name ='test')
print('---------------')

# 不定长参数
# 一个星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
def h6(arg1,*vartuple):
    print('输出：')
    print(arg1)
    for var in vartuple:
        print(var)
    return

h6(10)
h6(70,80,90)
print('---------------')

# 单独出现星号 * 后的参数必须用关键字传入
def h7(a,b,*,c):
    return a + b + c

# h7(1, 2, 3)   #报错
h8 = h7(1, 2, c=3)
print(h8)
print('---------------')

# 两个星号 ** 的参数会以字典的形式导入
def h9(arg1, **vardict):
    print(arg1)
    print(vardict)

h9(1,b = 2, c = 3)

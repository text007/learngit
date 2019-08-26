
# 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段
# 函数能提高应用的模块性，和代码的重复利用率

# 自定义一个函数规则
'''
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
'''

# 语法格式：定义函数使用 def 关键字
# 计算面积函数
def area(width, height):
    return width * height

def h1(name):
    print('welcom', name)

h1('abcd')
w = 4
h = 5
print('width = ', w,'height = ', h,'area =', area(w, h))
print('---------------')

# 函数调用
def h2(strs):  # 定义一个黄函数
    print(strs)
    return

h2('调用函数')
h2('调用函数')
print('---------------')

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
print('---------------')

# 匿名函数
# python 使用 lambda 来创建匿名函数
sum1 = lambda arg1, arg2: arg1 + arg2
print(sum1(10, 20))
print('---------------')

# return语句
# 退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None
def sum2(arg1, arg2):
    total = arg1 + arg2
    print('内：', total)
    return total    # 返回 total 的值

total = sum2(10, 20)
print('外：', total)
print('---------------')

# 变量作用域
# 程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的
'''
L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内置作用域（内置函数所在模块的范围）
只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问
'''
if True:
    msg = 'abc'
print(msg)

def test():
    msg_inner = 'ABC'
# print(msg_inner)  # 访问报错
print('---------------')

# 全局变量和局部变量
# 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
# 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。
# 调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。

total1 = 0  #全局变量
def sum3(arg1,arg2):
    total1 = arg1 +arg2 #局部变量
    print('内变量：', total1)
    return total1

sum3(10,20)
print('外变量：', total1)
print('---------------')

# global 和 nonlocal 关键字
# 修改全局变量
num = 1
def fun1():
    global num  # 声明修改全局变量
    print(num)
    num = 123
    print(num)
fun1()
print(num)
print('---------------')

# 修改嵌套作用域（enclosing 作用域，外层非全局作用域）
def outer():
    num = 10
    def inner():
        nonlocal num    # 声明修改局部变量
        num = 100
        print(num)
    inner()
    print(num)
outer()

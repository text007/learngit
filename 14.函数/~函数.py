
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


# del用法(删除)
var1 = 1
var2 = 10
print(var1, var2)

del var1    #删除var1
# print(var1)
print(var2)
print('------------------------------')


# 数值类型
'''
整型(lnt) - 通常被称为是整型或整数，是正或负整数，不带小数点。
浮点型(float) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
复数( (complex)) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。
'''

# 数字类型转换
'''
int(x) 将x转换为一个整数。
float(x) 将x转换到一个浮点数。
complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。
'''
a = 1.0
print(int(a))   #输出转换类型后的数字
print('------------------------------')


# 数字运算
print(2 + 2)            #加
print(50 - 5 * 6)       #减，乘
print((50 - 5 * 6) / 4) #减，乘，除
print(8 / 5)            #除，返回一个浮点数
print(7 // 2)           #除，只返回整数分部分
print(7.0 // 2.0)       #除，返回向下取整后的结果

print('------------------------------')


# = 赋值
width = 20
height = 5 * 9
print(width * height)
print('------------------------------')


# ** 幂运算
print(5 ** 2)   #5的平方
print(2 ** 7)   #2的7次方
print('------------------------------')


# 数字函数
'''
abs(x)	        返回数字的绝对值，如abs(-10) 返回 10
ceil(x)	        返回数字的上入整数，如math.ceil(4.1) 返回 5
exp(x)	        返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)	        返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)	    返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)	        如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)	    返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
modf(x)	        返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)	    x**y 运算后的值。
round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)	        返回数字x的平方根。
'''

import math     
print(abs(-10))                     #返回绝对值
print(math.ceil(4.5))               #向上取整
print(math.exp(1))                  #e的x次幂
print(math.fabs(-10))               #返回浮点数绝对值
print(math.floor(5.9))              #向下取整
print(math.log(100, 10))            #以10为底100的对数
print(math.log10(100))              #以10为底100的对数
print(max(1, 6, -1, -2.2, 0, 22/3)) #返回最大值
print(min(1, 6, -1, -2.2, 0, 22/3)) #返回最小值
print(math.modf(-2.2))              #返回整数部分和小数部分
print(pow(2, 3))                    #2的3次幂
print(round(17 / 3 , 2))            #四舍五入取2位小数
print(math.sqrt(2))                 #返回2的平方根
print('------------------------------')


#随机数函数
'''
choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
random()	随机生成下一个实数，它在[0,1)范围内。
seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	将序列的所有元素随机排序
uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。
''' 
import random
print(random.choice(range(10)))     #0-9随机数
print(random.randrange(1, 100, 2))  #1-100随机奇数
print(random.randrange(10))         #0-9随机数
print(random.random())              #[0，1]随机浮点数

list1 = [20, -10, 10, 5]
random.shuffle(list1)
print(list1)                        #随机排序
print(random.uniform(5, 10))        #5-10随机浮点数
print('------------------------------')


#三角函数
'''
acos(x)     返回x的反余弦弧度值。
asin(x)	    返回x的反正弦弧度值。
atan(x)	    返回x的反正切弧度值。
atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
cos(x)	    返回x的弧度的余弦值。
hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)	    返回的x弧度的正弦值。
tan(x)	    返回x弧度的正切值。
degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)	将角度转换为弧度
'''

import math

print(math.acos(-1))            #返回-1的反余弦弧度值
print(math.asin(1))             #返回1的反正弦弧度值
print(math.atan(0))             #返回0的反正切弧度值
print(math.atan2(-10, 10))      #返回给定的-10及10坐标值的反正切值
print(math.cos(0))              #返回0的弧度的余弦值
print(math.hypot(0, 2))         #返回欧几里德范数
print(math.sin(math.pi/2))      #返回π/2的弧度的正弦值
print(math.sin(3))              #返回的3弧度的正弦值
print(math.tan(math.pi/2))      #返回π/2的弧度正切值
print(math.tan(3))              #返回3弧度的正切值
print(math.degrees(math.pi))    #将π弧度转换为角度
print(math.radians(math.pi/4))  #将π/4角度转换为弧度


# 数学常量
'''
pi = π = 3.1415926535898
e = 自然常数 = 2.718281828459
'''

# 数字格式化
'''
3.1415926	{:.2f}	3.14	保留小数点后两位
3.1415926	{:+.2f}	+3.14	带符号保留小数点后两位
-1	        {:+.2f}	-1.00	带符号保留小数点后两位
2.71828	    {:.0f}	3	    不带小数
5	        {:0>2d}	05	    数字补零 (填充左边, 宽度为2)
5	        {:x<4d}	5xxx	数字补x (填充右边, 宽度为4)
10	        {:x<4d}	10xx	数字补x (填充右边, 宽度为4)
1000000	    {:,}	1,000,000	以逗号分隔的数字格式
0.25	    {:.2%}	25.00%	百分比格式
1000000000	{:.2e}	1.00e+09	指数记法
13	        {:>10d}	        13	右对齐 (默认, 宽度为10)
13	        {:<10d}	13	左对齐 (宽度为10)
13	        {:^10d}	    13	中间对齐 (宽度为10)
11	
'{:b}'.format(11)   1011        	进制
'{:d}'.format(11)   11
'{:o}'.format(11)   13
'{:x}'.format(11)   b
'{:#x}'.format(11)  0xb
'{:#X}'.format(11)	0XB
'''

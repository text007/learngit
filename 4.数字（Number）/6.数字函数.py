
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

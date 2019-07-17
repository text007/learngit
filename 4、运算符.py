# 算数运算符
'''
+	加 - 两个对象相加
-	减 - 得到负数或是一个数减去另一个数
*	乘 - 两个数相乘或是返回一个被重复若干次的字符串
/	除 - x 除以 y
%	取模 - 返回除法的余数
**	幂 - 返回x的y次幂
//	取整除 - 向下取接近除数的整数	
'''
a = 21
b = 10
c = 0

print('a + b = ',a + b)     #加
print('a - b = ',a - b)     #减
print('a * b = ',a * b)     #乘
print('a / b = ',a / b)     #除
print(r'a % b = ',a % b)    #取模
print('a ** b = ',a ** b)   #幂
print('a // b = ',a // b)   #取整除  

print('------------------------------')


# 比较运算符

'''
==	等于 - 比较对象是否相等	(a == b) 返回 False或True。
!=	不等于 - 比较两个对象是否不相等	(a != b) 返回 False或True。
>	大于 - 返回x是否大于y	(a > b) 返回 False或True。
<	小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。	(a < b) 返回 True。
>=	大于等于 - 返回x是否大于等于y。	(a >= b) 返回 False或True。
<=	小于等于 - 返回x是否小于等于y。	(a <= b) 返回 False或True。
'''

a = 21
b = 10
c = 0

# ==：是否等于
if (a == b):
    print('a 等于 b')
else:
    print('a 不等于 b')

# ！=是否不等于
if (a != b):
    print('a 不等于 b')
else:
    print('a 等于 b')

# <是否小于
if (a < b):
    print('a 小于 b')
else:
    print('a 大于等于 b')

# >是否大于
if (a > b):
    print('a 大于 b')
else:
    print('a 小于等于 b')

# <=是否小于等于
if (a <= b):
    print('a 小于等于 B')
else:
    print('a 大于 b')

# >=是否大于等于
if (a >= b):
    print('a 大于等于 b')
else:
    print('a 小于 b')

print('------------------------------')


# 赋值运算符
'''
=	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
+=	加法赋值运算符	c += a 等效于 c = c + a
-=	减法赋值运算符	c -= a 等效于 c = c - a
*=	乘法赋值运算符	c *= a 等效于 c = c * a
/=	除法赋值运算符	c /= a 等效于 c = c / a
%=	取模赋值运算符	c %= a 等效于 c = c % a
**=	幂赋值运算符	c **= a 等效于 c = c ** a
//=	取整除赋值运算符	c //= a 等效于 c = c // a
'''

a = 21
b = 10
c = 0

# = 赋值
c = a + b
print('a + b = c, c = ', c)

# += 加法赋值，等效于 c = c + a
c += a
print('c += a, c = ', c)

# -= 减法赋值,等效于 c = c - a
c -= a
print('c -= a, c = ', c)

# *= 乘法赋值运,等效于 c = c * a
c *= a
print('c *= a, c = ', c)

# /= 除法赋值,等效于 c = c / a
c /= a
print('c /= a, c = ', c)

c = 2
# %= 取模赋值,等效于 c = c % a
c %= a
print('c %= a, c = ', c)

# **= 幂赋值,等效于 c = c ** a
c **= a
print('c **= a, c = ', c)

# //= 取整除赋值,等效于 c = c // a
c //= a
print('c //= a, c = ', c)

print('------------------------------')


# 位运算符：对其二进制运算
'''
&	按位与：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
|	按位或：只要对应的二个二进位有一个为1时，结果位就为1,否则为0
^	按位异或：当两对应的二进位相异时，结果为1,否则为0
~	按位取反：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1
<<	左移动：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。
>>	右移动：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数
'''

a = 60      # 60 = 0011 1100
b = 13      # 13 = 0000 1101
c = 0

# &	按位与:11=1,10=0
c = a & b   # 12 = 0000 1100
print('a & b = ', c)

# |	按位或:10=1,11=1,00=0
c = a | b   # 61 = 0011 1101
print('a | b = ', c)

# ^	按位异或:10=1,11=0,00=0
c = a ^ b   # 49 = 0011 0001
print('a ^ b', c)

# ~	按位取反:0=1,1=0
c = ~a      # -61 = 1100 0011
print('~a = ', c)

# << 左移动:左移动n
c = a << 2  # 240 = 1111 0000
print('a << 2', c)

# >> 右移动：右移动n
c = a >> 2  # 15 = 0000 1111
print('a >> 2 =', c)

print('------------------------------')


# 逻辑运算符
'''
and x and y 布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。
or	x or y	布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。
not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。
'''
a = 10
b = 20

# true and true = true
if ( a and b ):
   print ("a and b 都为 true,", a and b)
else:
   print ("a and b 有一个不为 true,", a and b)
 
 # true or true = true
if ( a or b ):
   print ("a or b 都为 true，或其中一个为 true,", a or b)
else:
   print ("a or b 都不为 true,", a or b)
 
# 修改变量 a 的值
a = 0
# false and true = false
if ( a and b ):
   print ("a and b 都为 true,", a and b)
else:
   print ("a and b 有一个不为 true,", a and b)
 
#  false or true = true
if ( a or b ):
   print ("a or b 都为 true，或其中一个为 true,", a or b)
else:
   print ("a or b 都不为 true,", a or b)
 
#  not false = true, not true = false
if not( a and b ):
   print ("not(a and b) 都为 false，或其中一个为 false,", not( a and b ))
else:
   print ("not(a and b) 都为 true,", not( a and b ))
   
print('------------------------------')

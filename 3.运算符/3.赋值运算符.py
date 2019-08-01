
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

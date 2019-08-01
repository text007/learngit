
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

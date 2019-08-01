
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

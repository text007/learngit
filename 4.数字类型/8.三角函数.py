
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

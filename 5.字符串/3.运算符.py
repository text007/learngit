
# 字符串运算符
'''
+	    字符串连接
*	    重复输出字符串
[]	    通过索引获取字符串中字符
[ : ]	截取字符串中的一部分，遵循左闭右开原则，str[0,2] 是不包含第 3 个字符的。
in	    成员运算符 - 如果字符串中包含给定的字符返回 True
not in	成员运算符 - 如果字符串中不包含给定的字符返回 True
r/R	    原始字符串
%	    格式字符串（下一节）
'''

a = 'hello'
b = '1234'
print(a + b)            #字符串连接
print(a * 2)            #重复输出字符串
print(a[1])             #取字符串中字符
print(a[1:4])           #取字符串中连续字符

if('H' in a):           #是在变量a中
    print('H在变量a中')
else:
    print('H不在变量a中')

if ('M' not in a):       #不在变量a中
    print('M不在变量a中')
else:
    print('M在变量a中')

print(r'\n')            #原始字符串
print(R'\n')            #原始字符串

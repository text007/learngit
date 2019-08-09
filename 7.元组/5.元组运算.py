
# 元组运算符
'''
len((x))            计算元素个数
(x) + (m)           连接
(x,) * n            复制
x in (x)	        元素是否存在(True)
for x in (n): print (x,)      迭代
'''

print(len((1, 2, 3)))
print((12,)+(23, 45))
print((12,) * 2)
for x in (1, 2, 3):print(x,end='')

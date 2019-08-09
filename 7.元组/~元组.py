
# 元组使用小括号，使用逗号隔开
# 元组的元素不能修改
# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
# type(tup)查看数据类型
tup1 = (50)
print(tup1)
tup2 = (50,)
print(tup2)
print('------------------------------')

# 访问元组
tup3 = ('abc', 'ABC', 123)
tup4 = (1, 2, 3, 4, 5)
print(tup3[0])
print(tup4[1:6])
print('------------------------------')

# 修改元组
# 组中的元素值是不允许修改，但可以连接组合
tup5 = (12, 34, 56)
tup6 = ('abc', '123')
print(tup5 + tup6)
print('------------------------------')

# 删除元组
# 元组中的元素值是不允许删除的，但可以使用del语句来删除整个元组
tup7 = ('abc', 'ABC', 123)
del tup7
# print(tup7)       # 删除元组输出抛异常
print('------------------------------')

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
print('')
print('------------------------------')

# 元组索引，截取
tup8 = ('abc', 123, 'QWE')
print(tup8[1])
print(tup8[1:2])
print('------------------------------')

# 元组内置函数
'''
len(tuple)  计算元组元素个数	
max(tuple)  返回元组中元素最大值	
min(tuple)  返回元组中元素最小值	
tuple(seq)  将列表转换为元组
'''
tup9 = (123, 'abc', 'ABC')
tup10 = ('4', '5', '3')
list1 = [123, 'abc']
print(len(tup9))
print(max(tup10))
print(min(tup10))
print(tuple(list1))

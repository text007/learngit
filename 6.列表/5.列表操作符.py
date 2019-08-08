
# 列表脚本操作符
'''
len([x])        x长度
[x] + [n]	    [x, n]组合
['x'] * n	    [x][x][x]...n 重复
x in [x]	    True元素是否存在于列表中
for x in [1, 2, 3]: print(x, end=" ")	1 2 3	迭代
'''
print(len([1, 2, 3]))
print([1,2,3] + [3, 4, 5])
print([1, 2.2, 3] * 2)
print(2 in [1, 2, -2, 3])
for x in [1, 2, 3]:print(x, end='')# 把列表迭代给x(把列表元素分别赋值给x)
print('\n')

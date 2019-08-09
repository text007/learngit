
# 列表
'''
创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可
'''
list1 = ['google', '123']
list2 = [1, 2, 3, 4]
list3 = ['A','b','c',]
print('------------------------------')

# 访问列表中的值
list1 = ['google', '123']
list2 = [1, 2, 3, 4]
print(list1[1])
print(list2[1:3])
print('------------------------------')

# 更新列表
list4 = ['google', '123']
list4[1] = 2019
print(list4[1])
print(list4)
print('------------------------------')

# 删除列表元素
# 使用 del 语句来删除列表的的元素
list5 = ['google', 123]
del list5[1]
print(list5)
print('------------------------------')

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
print('------------------------------')

# 列表截取与拼接
l = ['google', 123, '345']
print(l[2])
print(l[-2])
print(l[1:])
print('------------------------------')

# 嵌套列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
b = [a, n]
print(b)
print(b[0][1])
print('------------------------------')

# 列表方法/方法
'''
len(list)               列表元素个数
max(list)               返回列表元素最大值
min(list)               返回列表元素最小值
list(seq)               将元组转换为列表
list.append(obj)        在列表末尾添加新的对象
list.count(obj)         统计某个元素在列表中出现的次数
list.extend(seq)        在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj)         从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj) 将对象插入列表
list.pop([index=-1])    移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj)        移除列表中某个值的第一个匹配项
list.reverse()          反向列表中元素
list.sort( key=None, reverse=False)     对原列表进行排序
list.clear()            清空列表
list.copy()             复制列表
'''
l1 = [1, 2, 3]
str1 = (11, 'aa')
print(len(l1))      # 列表元素个数
print(max(l1))      # 返回列表元素最大值
print(min(l1))      #返回列表元素最小值
print(list(str1))   #将元组转换为列表


# append()方法:用于在列表末尾添加新的对象
list6 = ['google', 123, 'taobao']
list6.append('baidu')
print(list6)

# count()方法:用于统计某个元素在列表中出现的次数
list7 = [123, 'abc', 123, 'abc', 123]
print(list7.count(123))

# extend()函数:用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list8 = [123, 'abc', 123]
list9 = list(range(5))      # 创建 0-4 的列表
list8.extend(list9)         # 扩展列表
print(list8)

# index()函数:用于从列表中找出某个值第一个匹配项的索引位置
list9 = ["123", 'abc', 123]
print(list9.index(123))

# insert()函数:用于将指定对象插入列表的指定位置
list10 = ["123", 'abc', 123]
list10.insert(1, 123)       # 在1的位置加入123 
print(list10)

# pop()函数：用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list11 = ["123", 'abc', 123]
list11.pop()        # 默认最后一个元素
print(list11)
list11.pop(0)       # 删除第0位置的元素
print(list11)

# remove()函数：用于移除列表中某个值的第一个匹配项
list12 = [123, "123", 'abc', 123]
list12.remove(123)
print(list12)

# reverse()函数:用于反向列表中元素
list13 = ["123", 'abc', 123]
list13.reverse()
print(list13)

# sort()函数:用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数
# reverse = True 降序， reverse = False 升序（默认）
def takesecond(elem):           # 获取列表中元组的第二个元素
    return elem[1]

random = [(2,2), (3,4), (4,1), (1,3)]
random.sort(key = takesecond)   # 指定第二个元素排序
print(random)

# clear()函数：用于清空列表，类似于 del a[:]
list14 = ["123", 'abc', 123]
del list14[:]
print(list14)
list15 = ["123", 'abc', 123]
list15.clear()
print(list15)

# copy()函数：用于复制列表，类似于 a[:]
list16 = ["123", 'abc', 123]
list17 = list16.copy()
print(list17)
list18 = list16[:]
print(list18)

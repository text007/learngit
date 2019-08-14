
# 集合（set）是一个无序的不重复元素序列
# 使用大括号 { } 或者 set() 函数创建集合
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
set1 = {'a', 'b', 1, 2, 'b', 2}
set2 = set('abcd')
print(set1)         # 去重功能
print(set2)
print('c' in set1)  # 元素是否在集合内
print(2 in set1)

# 集合运算.
'''
a - b   集合a中包含而集合b中不包含的元素
a | b   集合a或b中包含的所有元素
a & b   集合a和b中都包含了的元素
a ^ b   不同时包含于a和b的元素
'''
set3 = {'a', 'b', 1, 2, 'b', 2}
set4 = set('abcd')
print(set3 - set4)      # set3 有而 set4 没有的元素
print(set3 | set4)      # set3 和 set4 所有不重复的元素
print(set3 & set4)      # set3 和 set4 相同的元素
print(set3 ^ set4)      # set3 和 set4 不相同的元素

# 添加元素
# add（）
set5 = {'a', 'b', 1, 2, 'b', 2}
set5.add('c')
print(set5)

# s.update(x):参数可以是列表，元组，字典等
set6 = {'a', 'b', 1, 2, 'b', 2}
set6.update({1,3},[2,4])
print(set6)

# 移除元素
# s.remove(x)
set7 = {'a', 'b', 1, 2, 'b', 2}
set7.remove(2)
print(set7)
# set7.remove('c')    # 元素不存在,返回错误
# print(set7)

# s.discard(x):元素不存在,不会报错
set7 = {'a', 'b', 1, 2, 'b', 2}
set7.discard('c')
print(set7)

# s.pop():随机删除一个元素
set8 = {'a', 'b', 1, 2, 'b', 2}
x = set8.pop()
print(set8)
print(x)

# 计算集合元素个数
# len(s)
set9 = {'a', 'b', 1, 2, 'b', 2}
print(len(set9))

# 清空集合
# s.clear()
set10 = {'a', 'b', 1, 2, 'b', 2}
set10.clear()
print(set10)    # 返回一个空集合

# 判断元素是否在集合中
# x in s
set11 = {'a', 'b', 1, 2, 'b', 2}
print(2 in set11)
print('2' in set11)

# 内置方法
'''
add()               为集合添加元素
clear()             移除集合中的所有元素
copy()              拷贝一个集合
difference()	    返回多个集合的差集
difference_update()	移除集合中的元素，该元素在指定的集合也存在。
discard()	        删除集合中指定的元素
intersection()	    返回集合的交集
intersection_update()	返回集合的交集。
isdisjoint()	    判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	        判断指定集合是否为该方法参数集合的子集。
issuperset()	    判断该方法的参数集合是否为指定集合的子集
pop()	            随机移除元素
remove()	        移除指定元素
symmetric_difference()	返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	            返回两个集合的并集
update()	        给集合添加元素
'''

# add()方法:用于给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作
set11 = {'a', 'b', 1, 2}
set11.add('c')      # 添加元素
print(set11)
set11.add(2)        # 添加已存在的元素，则不执行
print(set11)

# clear()方法：用于移除集合中的所有元素
set12 = {'a', 'b', 1, 2}
set12.clear()
print(set12)    # 返回一个空集合

# copy()方法：用于拷贝一个集合
set13 = {'a', 'b', 1, 2}
set14 = set13.copy()
print(set14)

# difference()方法:用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中
set15 = {'a', 'b', 1, 2}
set16 = {'a', 'c', 3, 2}
set17 = set15.difference(set16) #与 a - b 相同，set15 有而 set16 没有
print(set17)

# difference_update()方法：用于移除两个集合中都存在的元素
# ifference_update() 方法与 difference() 方法的区别在于 difference() 方法返回一个移除相同元素的新集合，
# 而 difference_update() 方法是直接在原来的集合中移除元素，没有返回值。
set18 = {'a', 'b', 1, 2}
set19 = {'a', 'c', 3, 2}
set18.difference_update(set19)
print(set18)

# discard()方法:用于移除指定的集合元素
set20 = {'a', 'b', 1, 2}
set20.discard('a')
print(set20)

# intersection()方法:用于返回两个或更多集合中都包含的元素，即交集
set21 = {'a', 'b', 1, 2}
set22 = {'a', 'c', 3, 2}
set23 = set21.intersection(set22)
print(set23)

# intersection_update()方法:用于获取两个或更多集合中都重叠的元素，即计算交集
# intersection_update() 方法不同于 intersection() 方法，因为 intersection() 方法是返回一个新的集合，
# 而 intersection_update() 方法是在原始的集合上移除不重叠的元素
set23 = {'a', 'b', 1, 2}
set24 = {'a', 'c', 3, 2}
set23.intersection_update(set24)
print(set23,'\n')

# isdisjoint()方法:用于判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False
set25 = {'a', 'b', 1, 2}
set26 = {'c', 3}
set27 = set25.isdisjoint(set26)
print(set27)


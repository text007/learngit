
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

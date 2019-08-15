
# 集合（set）是一个无序的不重复元素序列
# 使用大括号 { } 或者 set() 函数创建集合
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
set1 = {'a', 'b', 1, 2, 'b', 2}
set2 = set('abcd')
print(set1)         # 去重功能
print(set2)
print('c' in set1)  # 元素是否在集合内
print(2 in set1)

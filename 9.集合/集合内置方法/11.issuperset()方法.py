
# issuperset()方法:用于判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False
set31 = {'a', 'b', 1, 2}
set32 = {'a', 1}
set33 = set31.issuperset(set32)
print(set33)

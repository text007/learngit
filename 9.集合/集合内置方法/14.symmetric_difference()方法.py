
# symmetric_difference()方法：返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素
set36 = {'a', 'b', 1, 2}
set37 = {'a', 'c', 3, 2}
set38 = set36.symmetric_difference(set37)   # 移除两个集合中都存在的元素
print(set38)

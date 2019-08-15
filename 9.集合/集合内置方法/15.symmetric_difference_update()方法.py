
# symmetric_difference_update()方法:移除当前集合中在另外一个指定集合相同的元素，
# 并将另外一个指定集合中不同的元素插入到当前集合中
set39 = {'a', 'b', 1, 2}
set40 = {'a', 'c', 3, 2}
set39.symmetric_difference_update(set40)    # 移除两个集合中都存在的元素，并将 set40 的元素添加到 set39 中
print(set39)

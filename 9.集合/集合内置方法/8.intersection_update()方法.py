
# intersection_update()方法:用于获取两个或更多集合中都重叠的元素，即计算交集
# intersection_update() 方法不同于 intersection() 方法，因为 intersection() 方法是返回一个新的集合，
# 而 intersection_update() 方法是在原始的集合上移除不重叠的元素
set23 = {'a', 'b', 1, 2}
set24 = {'a', 'c', 3, 2}
set23.intersection_update(set24)
print(set23)

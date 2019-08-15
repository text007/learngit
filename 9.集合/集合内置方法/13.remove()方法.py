
# remove()方法:用于移除集合中的指定元素
# 该方法不同于 discard() 方法，因为 remove() 方法在移除一个不存在的元素时会发生错误，而 discard() 方法不会
set35 = {'a', 'b', 1, 2}
set35.remove('b')
print(set35)
# set35.remove('c') #删除不存在的报错
# print(set35)

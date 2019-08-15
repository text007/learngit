
# difference()方法:用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中
set15 = {'a', 'b', 1, 2}
set16 = {'a', 'c', 3, 2}
set17 = set15.difference(set16) #与 a - b 相同，set15 有而 set16 没有
print(set17)

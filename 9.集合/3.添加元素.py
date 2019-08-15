
# 添加元素
# add（）
set5 = {'a', 'b', 1, 2, 'b', 2}
set5.add('c')
print(set5)

# s.update(x):参数可以是列表，元组，字典等
set6 = {'a', 'b', 1, 2, 'b', 2}
set6.update({1,3},[2,4])
print(set6)

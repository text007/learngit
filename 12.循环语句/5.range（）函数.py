
# 需要遍历数字序列，可以使用内置range()函数，会生自动成数列
for i in range(5):
    print(i)

print('--------------------')

# 可以使用range指定区间的值
for i in range(2, 5):
    print(i)

print('--------------------')

# 可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长')
for i in range(0, 10, 3):
    print(i)

print('--------------------')

for i in range(-10, -100, -30):
    print(i)

print('--------------------')

# range()和len()函数以遍历一个序列的索引
lan = ['C', 'C++', 'python', 'php']
for i in range(len(lan)):   # 使用数列来标识lan元素的个数
    print(i, lan[i])    # 使用数列作为索引，输出对应元素

print('--------------------')

# 使用range()函数来创建一个列表，元组,集合
print(list(range(5)))   #列表
print(tuple(range(5)))  #元组
print(set(range(5)))    #集合
print('--------------------')

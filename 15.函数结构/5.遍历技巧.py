
# items() 方法可以同时解读字典遍历中关键字和对应的值
knig = {'a':'1', 'b':'2'}
for k, v in knig.items():
    print(k, v)

print('---------------------')

# enumerate() 方法可以同时解读序列遍历中关键字和对应的值
for i, v in enumerate(['a','b','c']):
    print(i, v)

print('---------------------')

# zip() 同时遍历两个或更多的序列
que = ['a','b','c','d']
ans = ['1','2','3','4']
for q, a in zip(que,ans):
    print('字母是{0}，数字是{1}。'.format(q, a))    # str.format() 格式化函数, {} 来代替以前的 % 

print('---------------------')

# reversed() 反向遍历一个序列
for i in reversed(range(1, 10, 2)):
    print(i)

print('---------------------')

# sorted() 返回一个已排序的序列，并不修改原值
bas = ['a', 'b', 'c', '1', '2', '3']
for f in sorted(set(bas)):
    print(f)

print('---------------------')

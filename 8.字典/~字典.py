
# 字典
# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值(key=>value)对用冒号(:)分割，对之间用逗号(,)分割，字典用花括号({})表示 
# d = {key1 : value1, key2 : value2 }
# 键必须是唯一的，但值则不必
dict1 = {'Alice': '1234', 'Beth': '1234', 'Cecil': '1234'}
print(dict1)

# 访问字典值
dict2 = {'a':'1','b':'2','c':'3'}
print(dict2['c'])
# print(dict2['d'])     # 使用不存在的键访问数据，会输出错误

# 修改字典
dict3 = {'a':'1','b':'2','c':3}
dict3['a'] = 8
print(dict3)

# 删除字典元素
dict4 = {'a':'1','b':'2','c':3}
del dict4['c']  #删除键'c'
print(dict4)
dict4.clear()   #清空字典
print(dict4)
# del dict4     #删除字典会抛异常
# print(dict4)

# 字典的特性
# 1）不允许同一个键出现两次。
dict5 = {'a':'1','b':'2','a':3}
print(dict5)

# 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
dict6 = {('a',):'1', 3:'c'}
print(dict6)

# 字典内置函数
'''
len(dict)                           计算字典元素个数，即键的总数。	
str(dict)                           输出字典，以可打印的字符串表示。	
type(variable)                      返回输入的变量类型，如果变量是字典就返回字典类型。	
radiansdict.clear()                 删除字典内所有元素
radiansdict.copy()                  返回一个字典的浅复制
radiansdict.fromkeys()              创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
radiansdict.get(key, default=None)  返回指定键的值，如果值不在字典中返回default值
key in dict                         如果键在字典dict里返回true，否则返回false
radiansdict.items()                 以列表返回可遍历的(键, 值) 元组数组
radiansdict.keys()                  返回一个迭代器，可以使用 list() 来转换为列表
radiansdict.setdefault(key, default=None)   和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
radiansdict.update(dict2)           把字典dict2的键/值对更新到dict里
radiansdict.values()                返回一个迭代器，可以使用 list() 来转换为列表
pop(key[,default])                  删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
popitem()                           随机返回并删除字典中的一对键和值(一般删除末尾对)
'''

# len(dict)方法：计算字典元素个数，即键的总数
print(len({'a':'1','b':'2'}))

# str(dict)方法：输出字典，以可打印的字符串表示
dict7 = {'a':'1','b':'2'}
dict8 = str(dict7)
print(dict8)        #print默认打印的是str的格式，叫做用户友好打印
print(repr(dict8))  #repr后，是程序友好，就是实际的样子

# type(variable)方法：返回输入的变量类型
dict9 = {'a':'1','b':'2'}
print(type(dict9))

# clear()函数：用于删除字典内所有元素
dict10 = {'a':'1','b':'2'}
dict10.clear()
print(dict10)

# copy()函数:返回一个字典的浅复制
dict11 = {'a':'1','b':'2'}
dict12 = dict11.copy()
print(dict12)

# fromkeys()函数:用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值
seq = ('a', 'b', 'c')
dict13 = dict.fromkeys(seq,1)
print(dict13)

# get()函数:返回指定键的值，如果值不在字典中返回默认值
dict14 = {'a':'1','b':'2'}
print(dict14.get('b', 'c'))

# in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false
# not in 操作符刚好相反，如果键在字典 dict 里返回 false，否则返回 true
dict15 = {'a':'1','b':'2'}
if 'a' in dict15:
    print('存在')
else:
    print('不存在')

if 'c' not in dict15:
    print('不存在')
else:
    print('存在')

# items()方法：以列表返回可遍历的(键, 值) 元组数组
dict16 = {'a':'1','b':'2'}
print(dict16.items())

# keys()方法:返回一个可迭代对象，可以使用 list() 来转换为列表
dict17 = {'a':'1','b':'2'}
dict17.keys()
print(list(dict17.keys()))

# setdefault()方法:和 get()方法 类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值
dict18 = {'a':'1','b':'2'}
print(dict18.setdefault('a'))
dict18.setdefault('c', None)
print(dict18)

# update()函数：把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里
dict19 = {'a':'1','b':'2'}
dict20 = {'b':'2','c':'3'}
dict19.update(dict20)
print(dict19)

# values()方法:返回一个迭代器，可以使用 list() 来转换为列表，列表为字典中的所有值
dict21 = {'a':'1','b':'2'}
print(list(dict21.values()))

# pop()方法:删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值
dict22 = {'a':'1','b':'2'}
pop_obj = dict22.pop('a')
print(dict22)
print(pop_obj)  # 返回已删除的值

# popitem()方法:随机返回并删除字典中的一对键和值(一般删除末尾对)
# 如果字典已经为空，却调用了此方法，就报出KeyError异常
dict23 = {'a':'1','b':'2'}
pop_obj = dict23.popitem()
print(pop_obj)  # 返回已删除的值
print(dict23)


# 字典
# 字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))
print('guido' in tel)
print('jack' not in tel)
print('---------------------')

# 字典推导式
# dict 直接从键值对元组列表中构建字典
print(dict([('a',1),('b',2)]))

# 创建任意键和值
print({x:x**2 for x in (2, 4, 6)})

# 关键字参数指定键值对
print(dict(a = 1, b = 2, c = 3))
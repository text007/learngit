
# pop()方法:删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值
dict22 = {'a':'1','b':'2'}
pop_obj = dict22.pop('a')
print(dict22)
print(pop_obj)  # 返回已删除的值

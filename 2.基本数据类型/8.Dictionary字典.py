
# Dictionary（字典）
dict = {}
dict['one'] = '1 - day1'
dict[2] = '2 - day2'

tinydict = {'name':'runoob', 'code':1, 'site':'www.123.com'}

print(dict['one'])          # 输出键为 'one' 的值
print(dict[2])              # 输出键为 2 的值
print(tinydict)             # 输出完整的字典
print(tinydict.keys())      # keys() 输出所有键
print(tinydict.values())    # values() 输出所有值
print('------------------------------')

# 字典遍历
print({x: x**2 for x in (2, 4, 6)})     #对x取值进行平方，再进行x的遍历
print('------------------------------')

# clear()方法
dicts = {'Name': 'Zara', 'Age': 7}
print(len(dicts))       #字典元素个数
dicts.clear()           #clear()删除字典内所有元素
print(len(dicts))       #字典元素个数

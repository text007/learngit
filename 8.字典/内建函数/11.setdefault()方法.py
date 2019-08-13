
# setdefault()方法:和 get()方法 类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值
dict18 = {'a':'1','b':'2'}
print(dict18.setdefault('a'))
dict18.setdefault('c', None)
print(dict18)


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

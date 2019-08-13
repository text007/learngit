
# str(dict)方法：输出字典，以可打印的字符串表示
dict7 = {'a':'1','b':'2'}
dict8 = str(dict7)
print(dict8)        #print默认打印的是str的格式，叫做用户友好打印
print(repr(dict8))  #repr后，是程序友好，就是实际的样子


# 输出格式美化
# str()： 函数返回一个用户易读的表达形式
# repr()： 产生一个解释器易读的表达形式
s = 'abc123'
print(str(s))   #print默认打印的是str的格式，叫做用户友好打印
print(repr(str(s)))   #repr后，是程序友好，就是实际的样子

x = 10 * 3.25
y = 200 * 200
print(repr((x,y,('123','abc'))))
print('---------------------')

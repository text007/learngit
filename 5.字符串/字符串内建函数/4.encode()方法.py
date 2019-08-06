
# encode()方法：返回编码后的字符串
# bytes.decode()方法：返回解码后的字符串
str4 = '字符串'
str_utf8 = str4.encode('UTF-8')
str_gbk = str4.encode('GBK')

print(str4)

print(str_utf8)
print(str_gbk)

print(str_utf8.decode('UTF-8', 'strict'))
print(str_gbk.decode('GBK', 'strict'))

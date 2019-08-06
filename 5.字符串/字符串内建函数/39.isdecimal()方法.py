
# isdecimal()方法:检查字符串是否只包含十进制字符。这种方法只存在于unicode对象,只包含十进制字符返回True，否则返回False
# 注意:定义一个十进制字符串，只需要在字符串前添加 'u' 前缀即可
str58 = 'abcABC123'
print(str58.isdecimal())

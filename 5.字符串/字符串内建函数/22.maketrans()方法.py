
# maketrans()方法:用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，
# 第一个参数是字符串，表示需要转换的字符，
# 第二个参数也是字符串表示转换的目标。
# 两个字符串的长度必须相同，为一一对应的关系。
intad = 'aeiou'
outtad = '12345'
str30 = "this is string example....wow!!!"
trantad = str30.maketrans(intad, outtad)
print(str30.translate(trantad))


# split()方法：通过指定分隔符对字符串进行切片，如果第二个参数num有指定值，则分割为num+1个子字符串
str40 = "this is string example....wow!!!"
print(str40.split())            #把空格替换成（，）分隔，进行切片
print(str40.split('i', 2))      #把前 2 个 i 替换成（，）分隔

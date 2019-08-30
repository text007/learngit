
# 字符串 
# 使用引号( ' 或 " )来创建字符串

print('123')
print("字符串")
print('------------------------------')


# 访问字符串中的值
var1 = 'hello world!'
var2 = "123456"

print(var1[0])
print(var2[1:5])
print('------------------------------')


# 字符串更新
var1 = 'hello world!'
var2 = "123456"

print(var1[:6] + var2[:3])
print('------------------------------')


# 转义字符
r'''
r               保留原始字符串（防止转义）
\(在行尾时)      续行符
\\              反斜杠符号
\'	            单引号
\"	            双引号
\a	            响铃
\b	            退格(Backspace)
\000	        空
\n	            换行
\v	            纵向制表符
\t	            横向制表符
\r	            回车
\f	            换页
\oyy	        八进制数，yy 代表的字符，例如：\o12 代表换行，其中 o 是字母，不是数字 0。
\xyy	        十六进制数，yy代表的字符，例如：\x0a代表换行
\other	        其它的字符以普通格式输出
'''

print(r'D:\learngit\5.字符串')   #原始字符串

a1 = '123\
456'
print(a1)                       #续行符

print('\\')                     #反斜杠符号
print('a\nb')                   #换行
print('a\rb')                   #回车
print('------------------------------')


# 字符串运算符
'''
+	    字符串连接
*	    重复输出字符串
[]	    通过索引获取字符串中字符
[ : ]	截取字符串中的一部分，遵循左闭右开原则，str[0,2] 是不包含第 3 个字符的。
in	    成员运算符 - 如果字符串中包含给定的字符返回 True
not in	成员运算符 - 如果字符串中不包含给定的字符返回 True
r/R	    原始字符串
%	    格式字符串（下一节）
'''

a = 'hello'
b = '1234'
print(a + b)            #字符串连接
print(a * 2)            #重复输出字符串
print(a[1])             #取字符串中字符
print(a[1:4])           #取字符串中连续字符

if('H' in a):           #是在变量a中
    print('H在变量a中')
else:
    print('H不在变量a中')

if ('M' not in a):       #不在变量a中
    print('M不在变量a中')
else:
    print('M在变量a中')

print(r'\n')            #原始字符串
print(R'\n')            #原始字符串
print('------------------------------')


# 字符串格式
'''
%c	 格式化字符及其ASCII码
%s	 格式化字符串
%d	 格式化整数
%u	 格式化无符号整型
%o	 格式化无符号八进制数
%x	 格式化无符号十六进制数
%X	 格式化无符号十六进制数（大写）
%f	 格式化浮点数字，可指定小数点后的精度
%e	 用科学计数法格式化浮点数
%E	 作用同%e，用科学计数法格式化浮点数
%g	 %f和%e的简写
%G	 %f 和 %E 的简写
%p	 用十六进制数格式化变量的地址
format()    通过 {} 和 : 来代替以前的 %
'''

print('我叫 %s 今年 %d 岁！' % ('小米',15))
print('------------------------------')

# 格式化操作符辅助指令
'''
*	    定义宽度或者小数点精度
-	    用做左对齐
+	    在正数前面显示加号( + )
<sp>	在正数前面显示空格
#	    在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
0	    显示的数字前面填充'0'而不是默认的空格
%	    '%%'输出一个单一的'%'
(var)	映射变量(字典参数)
m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
'''

# str.format() 增强了字符串格式化的功能
print('{} {}'.format('hello','worid'))  # 不设置指定位置，按默认顺序

print('{0} {1}'.format('hello','worid'))    # 设置指定位置

print('{1} {0} {1}'.format('hello','worid'))    # 设置指定位置


# 字符串内建函数
'''
capitalize()
将字符串的第一个字符转换为大写

center(width, fillchar)
返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。

count(str, beg= 0,end=len(string))
返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

bytes.decode(encoding="utf-8", errors="strict")
Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。

encode(encoding='UTF-8',errors='strict')
以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'

endswith(suffix, beg=0, end=len(string))
检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
	
expandtabs(tabsize=8)
把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。

find(str, beg=0, end=len(string))
检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1

index(str, beg=0, end=len(string))
跟find()方法一样，只不过如果str不在字符串中会报一个异常.

isalnum()
如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False

isalpha()
如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False

isdigit()
如果字符串只包含数字则返回 True 否则返回 False..

islower()
如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False

isnumeric()
如果字符串中只包含数字字符，则返回 True，否则返回 False

isspace()
如果字符串中只包含空白，则返回 True，否则返回 False.

istitle()
如果字符串是标题化的(见 title())则返回 True，否则返回 False

isupper()
如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False

join(seq)
以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串

len(string)
返回字符串长度

ljust(width[, fillchar])
返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。

lower()
转换字符串中所有大写字符为小写.

lstrip()
截掉字符串左边的空格或指定字符。

maketrans()
创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。

max(str)
返回字符串 str 中最大的字母。

min(str)
返回字符串 str 中最小的字母。

replace(old, new [, max])
把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。

rfind(str, beg=0,end=len(string))
类似于 find()函数，不过是从右边开始查找.

rindex( str, beg=0, end=len(string))
类似于 index()，不过是从右边开始.

rjust(width,[, fillchar])
返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串

rstrip()
删除字符串字符串末尾的空格.

split(str="", num=string.count(str))
num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串

splitlines([keepends])
按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。

startswith(substr, beg=0,end=len(string))
检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。

strip([chars])
在字符串上执行 lstrip()和 rstrip()

swapcase()
将字符串中大写转换为小写，小写转换为大写

title()
返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())

translate(table, deletechars="")
根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中

upper()
转换字符串中的小写字母为大写

zfill (width)
返回长度为 width 的字符串，原字符串右对齐，前面填充0

isdecimal()
检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
'''

# capitalize()方法：第一个字母变成大写,其他字母变小写。
str1 = 'this is ... wow!!'
print(str1.capitalize())

# center()方法：指定的宽度，居中的字符串
str2 = '[www.baidu.com]'
print(str2.center(40, '-'))

# count()方法：统计字符串里某个字符出现的次数,搜索的开始与结束位置。
str3 = '[www.baidu.com]'
sub = 'w'
print(str3.count(sub, 0, 12))

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

# endswith()方法：判断字符串是否以指定后缀结尾
str5= 'Runoob example....wow!!!'
suffix1= '!!'
print(str5.endswith(suffix1,16))        #开始位置16
suffix2= 'w'
print(str5.endswith(suffix2, 0, 25))    #0开始，25结束

# expandtabs()方法：替换字符串中转义字符（\t）为空格
str6 = 'this\tis ... wow!!'
print(str6.expandtabs(1))   #替换为1个空格

# find()方法：检测字符串中是否包含子字符串,包含返回索引位置，不包含返回-1
str7 = 'Runoob example....wow!!!'
str8 = 'exa'

print(str7.find(str8,5))    #5起始，包含返回索引位置
print(str7.find(str8,10))   #10起始，不包含返回-1

# index()方法：检测字符串中是否包含子字符串,包含返回索引位置，不包含返回异常
str9 = 'Runoob example....wow!!!'
str10 = 'exa'

print(str9.index(str10,5))    #5起始，包含返回索引位置
# print(str9.index(str10,10))   #10起始，不包含返回异常

# isalnum()方法：检测字符串是否由字母和数字组成,返回True and False
str11 = 'abcd1234'
str12 = 'abcd 1234'
print(str11.isalnum())
print(str12.isalnum())

# isalpha()方法：检测字符串是否只由字母组成，返回True and False
str13 = 'abcd'
str14 = 'abcd1234'
print(str13.isalpha())
print(str14.isalpha())

# isdigit()方法：检测字符串是否只由数字组成，返回True and False
str15 = '123456'
str16 = 'abc123'
print(str15.isdigit())
print(str16.isdigit())

# islower()方法:检测字符串是否由小写字母组成，返回True and False
str17 = 'zbcde123'
str18 = 'Abc123'
print(str17.islower())  #只检测字母大小写
print(str18.islower())

# isnumeric():方法检测字符串是否只由数字组成，只针对unicode对象，返回True and False
str19 = u'123456'
str20 = u'abcd123'
print(str19.isnumeric())
print(str20.isnumeric())

# isspace()方法:检测字符串是否只由空白字符组成，返回True and False
str21 = '   '
str22 = 'a b c d'
print(str21.isspace())
print(str22.isspace())

# istitle()方法：检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写，返回True and False
str23 = 'This Is ... 123!!'
str24 = 'this is ... wow!!'
print(str23.istitle())
print(str24.istitle())

# isupper()方法:检测字符串中所有的字母是否都为大写
str25 = 'THIS IS ... 123!!'
str26 = "This Is ... 123!!"
print(str25.isupper())
print(str26.isupper())

#  join()方法：将序列中的元素以指定的字符连接生成一个新的字符串
s1 = '-'
s2 = ''
seq = ('a', 'b', 'c', 'd')
print(s1.join(seq))
print(s2.join(seq))

# len()方法：返回对象（字符、列表、元组等）长度或项目个数
print(len('abcde'))
print(len([1,2,3,4,5]))

# ljust()方法:返回原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
str27 = "This Is ... 123!!"
print(str27.ljust(25,'-'))

# lower()方法：转换字符串中所有大写字符为小写
str28 = 'ABCde'
print(str28.lower())

# lstrip()方法：用于截掉字符串左边的空格或指定字符。
str29 = "88888abc d"
print(str29.lstrip('8'))

# maketrans()方法:用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，
# 第一个参数是字符串，表示需要转换的字符，
# 第二个参数也是字符串表示转换的目标。
# 两个字符串的长度必须相同，为一一对应的关系。
intad = 'aeiou'
outtad = '12345'
str30 = "this is string example....wow!!!"
trantad = str30.maketrans(intad, outtad)
print(str30.translate(trantad))

# max()方法:返回字符串中最大的字母
str31 = 'Abcde123'
print(max(str31))

# min()方法:返回字符串中最小的字母
str32 = 'Abcde123'
print(min(str32))

# replace()方法:把字符串中的old（旧字符串）替换成new(新字符串)，如果指定第三个参数max，则替换不超过max次
str33 = "this is string example....this is...!!!"
print(str33.replace('is', 'was', 3))

# rfind()方法：返回字符串最后一次出现的位置，如果没有匹配项则返回-1
# find()方法：返回字符串第一次出现的位置，如果没有匹配项则返回-1
str34 = "this is string example....this is...!!!"
str35 = 'is'
print(str34.rfind(str35, 0, 10))
print(str34.rfind(str35, 10, 0))
print(str34.find(str35, 0, 10))
print(str34.find(str35, 10, 0))

# rindex()方法：返回子字符串str在字符串中最后出现的位置，如果没有匹配的字符串会报异常，可以指定可选参数[beg:end]设置查找的区间
str36 = "this is string example....!!!"
str37 = 'is'
print(str36.rindex(str37, 0 , 10))

# rjust()方法：返回一个原字符串右对齐,并使用空格填充至长度width的新字符串。指定的长度小于字符串的长度则返回原字符串。
str38 = 'qwer123'
print(str38.rjust(20, '-'))

# rstrip()方法：删除string字符串末尾的指定字符（默认为空格）
str39 = "------this is string example---------"
print(str39.rstrip('-'))

# split()方法：通过指定分隔符对字符串进行切片，如果第二个参数num有指定值，则分割为num+1个子字符串
str40 = "this is string example....wow!!!"
print(str40.split())            #把空格替换成（，）分隔，进行切片
print(str40.split('i', 2))      #把前 2 个 i 替换成（，）分隔

# splitlines()方法：按照行('\r','\r\n',\n')分隔，返回一个包含各行作为元素的列表，如果参数keepends为False，不包含换行符，如果为True，则保留换行符
str41 = 'ad c\n\nde fg\r\n'
print(str41.splitlines())
print(str41.splitlines(True))

# startswith()方法:用于检查字符串是否是以指定子字符串开头，如果是则返回True，否则返回False。如果参数 beg和 end指定值，则在指定范围内检查
str42 = "this is string example....wow!!!"
print(str42.startswith('this', 0, 4))

# strip()方法:用于移除字符串头尾指定的字符（默认为空格）或字符序列
# 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符
str43 = '123abcABC321'
print(str43.strip('12'))

# swapcase()方法:用于对字符串的大小写字母进行转换
str44 = '123abcABC321'
print(str44.swapcase())

# title()方法:返回"标题化"的字符串,就是说所有单词的首个字母转化为大写，其余字母均为小写
# 注意，非字母后的第一个字母将转换为大写字母
str45 = "this is hello b2b2b2 and 3g3g3g!!!"
print(str45.title())

# translate()方法:根据参数table给出的表(包含256个字符)转换字符串的字符,要过滤掉的字符放到deletechars参数中
# 制作翻译表：maketrans（）方法：b1与b2一一对应，相互转换; bytes()方法：创建字符节码
bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(b'abcdoob'.translate(bytes_tabtrans, b'o'))   # 转换为大写，并删除字母

# upper()方法：将字符串中的小写字母转为大写字母
str56 = 'abcABC123'
print(str56.upper())

# zfill()方法:返回指定长度的字符串，原字符串右对齐，前面填充0
str57 = 'abcABC123'
print(str57.zfill(15))

# isdecimal()方法:检查字符串是否只包含十进制字符。这种方法只存在于unicode对象,只包含十进制字符返回True，否则返回False
# 注意:定义一个十进制字符串，只需要在字符串前添加 'u' 前缀即可
str58 = 'abcABC123'
print(str58.isdecimal())

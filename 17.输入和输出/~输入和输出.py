
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

# 符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格
for x in range(1,11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=" ")
    print(repr(x*x*x).rjust(5))
    
print('---------------------')

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)) # 2d 两个空格

print('---------------------')

#  zfill() 方法
print('12'.zfill(5))
print('-3.14'.zfill(7))

# str.format() 用法
print('数字：{}，字母：{}！'.format('123','abc'))

#括号中的数字用于指向传入对象在 format() 中的位置
print('{0} 和 {1}'.format('123', 'abc'))
print('{1} 和 {0}'.format('123', 'abc'))
print('---------------------')

# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数
print('数字：{name}，字母：{site}！'.format(name = '123', site = 'abc'))

# 位置及关键字参数可以任意的结合
print('{0}, {1}, 和 {other}'.format('123', 'abc',other = '!!!'))

# !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化
import math
print('pi≈ {!r}'.format(math.pi))
print('---------------------')

# 可选项 : 和格式标识符可以跟着字段名
print('pi≈ {0:.3f}'.format(math.pi))  # 0:.3f 保留3位小数

# 在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用
table = {'a':1,'b':2,'c':3}
for name, number in table.items():
    print('{0:5} ==> {1:5d}'.format(name,number))   # items() 函数以列表返回可遍历的(键, 值) 元组数组

print('---------------------')

# 格式化时通过变量名
# 使用方括号 [] 来访问键值
table1 = {'a':1,'b':2,'c':3}
print('a:{0[a]:d}; b:{0[b]:d}; c:{0[c]:d}'.format(table1))

# 通过在 table 变量前使用 ** 来实现相同的功能
table2 = {'a':1,'b':2,'c':3}
print('a:{a:d}; b:{b:d}; c:{c:d}'.format(**table2))
print('---------------------')

# 旧式字符串格式化
import math
print('pi≈ %5.3f。' % math.pi)  # 5位字符，3位小数
print('---------------------')

# 读取键盘输入
# str1 = input('清输入：')
# print('你输入的内容是：', str1)

# 读和写文件
# open(filename, mode)
# filename：包含了你要访问的文件名称的字符串值。
# mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
'''
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
'''

f = open('D:/learngit/17.输入和输出/foo.txt', 'w')  # 打开一个文件
f.write('Python 是一个非常好的语言。\n是的，确实是非常好!!\n')  # 写让内容
f.close()   #关闭文件夹
print('---------------------')

# 文件对象的方法
# f.read() 将读取一定数目的数据, 然后作为字符串或字节对象返回
f = open('D:/learngit/17.输入和输出/foo.txt', 'r')  # 打开一个文件
str1 = f.read() # 文件内容赋值
print(str1) # 打印内容
f.close()   # 关闭文件
print('---------------------')

# f.readline() 从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行
f = open('D:/learngit/17.输入和输出/foo.txt', 'r')
str2 = f.readline() # 读取单独的一行
print(str2)
f.close()
print('---------------------')

# f.readlines() 返回该文件中包含的所有行
f = open('D:/learngit/17.输入和输出/foo.txt', 'r')
str3 = f.readlines()    # 读取全部内容，行之间用\n显示
print(str3)
f.close()
print('---------------------')

f = open('D:/learngit/17.输入和输出/foo.txt', 'r')
for line in f:  # 迭代文件内容，全部显示
    print(line, end='')

f.close()
print('---------------------')

# f.write(string) 将 string 写入到文件中, 然后返回写入的字符数
f = open('D:/learngit/17.输入和输出/foo.txt', 'w')
num = f.write('Python 是一个非常好的语言。\n是的，确实是非常好!!\n') # 写入内容，并返回字符数
print(num)
f.close()

f = open('D:/learngit/17.输入和输出/foo.txt', 'w')
value = ('www.baidu.com', 20190903)
s = str(value)
f.write(s)
f.close()
print('---------------------')

# f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数
f = open('D:/learngit/17.输入和输出/foo.txt', 'r')
p = f.tell()
print('当前位置：%d' % (p))
f.close()
print('---------------------')

# f.seek() 改变文件当前的位置
'''
seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
seek(x,1) ： 表示从当前位置往后移动x个字符
seek(-x,2)： 表示从文件的结尾往前移动x个字符
'''
f = open('D:/learngit/17.输入和输出/foo.txt', 'rb+')
print(f.write(b'0123456789abcdf'))  # 写入
print(f.seek(5))
print(f.read(1))
print(f.seek(-3,2))
print(f.read(1))
f.close()
print('---------------------')

# f.close() 关闭文件并释放系统的资源
f = open('D:/learngit/17.输入和输出/foo.txt', 'r')
f.close()
# p = f.read()  # 再次调用报错
# print(p)
print('---------------------')

# f.isatty() 方法检测文件是否连接到一个终端设备，如果是返回 True，否则返回 False
f = open('D:/learngit/17.输入和输出/foo.txt', 'r')
ret = f.isatty()
print(ret)
f.close()
print('---------------------')

# f.truncate() 方法用于截断文件并返回截断的字节长度
f = open('D:/learngit/17.输入和输出/foo.txt', 'w')
ret = f.truncate(3)
print(ret)
f.close()
print('---------------------')

# pickle 模块
# 实现基本的数据序列和反序列化
# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象
import pickle   # 导入模块
data1 = {'a':[1, 2.0, 3, 4+6j], # 创建一个字典
    'b':('s',u'Un'),
    'c':None}

s_l = [1, 2, 3] # 创建一个列表
s_l.append(s_l)     # 列表末尾添加一个列表

o = open('data.pk1', 'wb')  # 打开一个文件（没有就创建），读取写入

pickle.dump(data1, o)   # 用pickle模块使字典保存到文件中
pickle.dump(s_l, o, -1) # 用pickle模块使列表保存到文件中
o.close()   # 关闭文件

# load() 反序列化对象，将文件中的数据解析为一个python对象
import pprint, pickle  # 导入模块
p_f = open('data.pk1', 'rb')    # 打开文件
data2 = pickle.load(p_f)    # 反序列化文件对象
pprint.pprint(data2)    # 美化格式

data3 = pickle.load(p_f)    # 反序列化文件对象
pprint.pprint(data3)    # 美化格式

p_f.close() # 关闭文件

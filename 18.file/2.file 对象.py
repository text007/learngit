
# file 对象使用 open 函数来创建
'''
file.close()
关闭文件。关闭后文件不能再进行读写操作。

file.flush()
刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。

file.fileno()
返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。

file.isatty()
如果文件连接到一个终端设备返回 True，否则返回 False。

file.next()
Python 3 中的 File 对象不支持 next() 方法。
返回文件下一行。

file.read([size])
从文件读取指定的字节数，如果未给定或为负则读取所有。

file.readline([size])
读取整行，包括 "\n" 字符。

file.readlines([sizeint])
读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。

file.seek(offset[, whence])
设置文件当前位置
	
file.tell()
返回文件当前位置。
	
file.truncate([size])
从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除，其中 Widnows 系统下的换行代表2个字符大小。

file.write(str)
将字符串写入文件，返回的是写入的字符长度。

file.writelines(sequence)
向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
'''
# close() 方法用于关闭一个已打开的文件。关闭后的文件不能再进行读写操作， 否则会触发 ValueError 错误
fo = open('test.txt', 'wb')
print('文件名：', fo.name)
fo.close()  # 关闭文件
print('---------------------')

# flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入
# 文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法
fo = open('test.txt', 'wb')
fo.flush()  # 刷新缓冲区
fo.close()  # 关闭文件
print('---------------------')

# fileno() 方法返回一个整型的文件描述符(file descriptor FD 整型)，可用于底层操作系统的 I/O 操作
fo = open('test.txt', 'wb')
fid = fo.fileno()
print('文件描述符为：', fid)
fo.close()
print('---------------------')

# isatty() 方法检测文件是否连接到一个终端设备，如果是返回 True，否则返回 False。
fo = open('test.txt', 'wb')
ret = fo.isatty()
print('返回值：', ret)
fo.close()
print('---------------------')

# read() 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有
fo = open('test.txt', 'r+')
line = fo.read(10)
print('读取字符串：%s' % (line))
fo.close()
print('---------------------')

# readline() 方法用于从文件读取整行，包括 "\n" 字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n" 字符
fo = open('test.txt', 'r+')
line2 = fo.readline()
print('读取第一行：%s' % (line2))
line3 = fo.readline(5)
print('读取字符串：%s' % (line3))
fo.close()
print('---------------------')

# readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表，该列表可以由 Python 的 for... in ... 结构进行处理。 如果碰到结束符 EOF 则返回空字符串。
fo = open('test.txt', 'r')
for line4 in fo.readlines():    # 依次读取每行
    line4 = line4.strip()   # 去掉每行头尾空白
    print('读取的数据为：%s' % (line4))

fo.close()
print('---------------------')

# seek(offset[, whence]) 方法用于移动文件读取指针到指定位置
# offset -- 开始的偏移量，也就是代表需要移动偏移的字节数，如果是负数表示从倒数第几位开始。
# whence：可选，默认值为 0。给 offset 定义一个参数，表示要从哪个位置开始偏移；0 代表从文件开头开始算起，1 代表从当前位置开始算起，2 代表从文件末尾算起。
fo = open('test.txt', 'rb+')
line5 = fo.write(b'0123456789\nabcdef')   # 写入指定字符串
print(line5)
line6 = fo.seek(5)  # 移动到文件的第六个字节
print(line6)
line7 = fo.read(1)  # 读取指定的字节数
print(line7)
line8 = fo.seek(-3,2)   # 移动到文件倒数第三个字节
print(line8)
line9 = fo.read(1)  # 读取指定的字节数
print(line9)
fo.close()

# 循环读取文件的内容
fo = open('test.txt', 'r+')
line10 = fo.readline()
print('读取的数据为：%s' % (line10))
fo.seek(0,0)    # 重新设置文件读取指针到开头
line11 = fo.readline()
print('读取的数据为：%s' % (line11))
fo.close()
print('---------------------')

# tell() 方法返回文件的当前位置，即文件指针当前位置
fo = open('test.txt', 'r+')
line12 = fo.readline()
print('读取的数据为：%s' % (line12))
# fo.seek(5)
pos = fo.tell() # 获取当前文件位置
print('当前位置：%d' % (pos))
fo.close()
print('---------------------')

# truncate() 方法用于从文件的首行首字节开始截断，截断文件为 size 个字节，无 size 表示从当前位置截断；截断之后 V 后面的所有字节被删除，其中 Widnows 系统下的换行代表2个字节大小
fo = open('test.txt', 'r+')
line13 = fo.readline()  # 读取
print('读取行：%s' % (line13))
fo.truncate() # 截断首行
line14 = fo.readline()
print('读取行：%s' % (line14))
fo.close()
print('---------------------')

fo = open('test.txt', 'r+')
fo.truncate(10) # 截取10个字符
str1 = fo.read()
print('读取数据：%s ' %(str1))
fo.close()
print('---------------------')

# write() 方法用于向文件中写入指定字符串
fo = open('test1.txt', 'r+')
str2 = '\n6:第六行'
fo.seek(0,2)    # 文件末尾
line15 = fo.write(str2) # 写入字符
fo.seek(0, 0)   # 文件开头
for index in range(6):  
    line16 = next(fo)   # next() 返回文件的下一行
    print('文件行数 %d - %s' % (index, line16))

fo.close()
print('---------------------')

# writelines() 方法用于向文件中写入一序列的字符串
fo = open('test1.txt', 'w')
seq = ['abc\n','123\n','ABC123']
fo.writelines(seq)
fo.close()
print('---------------------')


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

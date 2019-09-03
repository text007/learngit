
# f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数
f = open('D:/learngit/17.输入和输出/foo.txt', 'r')
p = f.tell()
print('当前位置：%d' % (p))
f.close()
print('---------------------')

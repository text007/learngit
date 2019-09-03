
# f.isatty() 方法检测文件是否连接到一个终端设备，如果是返回 True，否则返回 False
f = open('D:/learngit/17.输入和输出/foo.txt', 'r')
ret = f.isatty()
print(ret)
f.close()
print('---------------------')

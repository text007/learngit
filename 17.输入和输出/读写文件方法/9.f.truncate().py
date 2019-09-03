
# f.truncate() 方法用于截断文件并返回截断的字节长度
f = open('D:/learngit/17.输入和输出/foo.txt', 'w')
ret = f.truncate(3)
print(ret)
f.close()
print('---------------------')


# f.read() 将读取一定数目的数据, 然后作为字符串或字节对象返回
f = open('D:/learngit/17.输入和输出/foo.txt', 'r')  # 打开一个文件
str1 = f.read() # 文件内容赋值
print(str1) # 打印内容
f.close()   # 关闭文件
print('---------------------')

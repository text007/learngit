
# f.readline() 从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行
f = open('D:/learngit/17.输入和输出/foo.txt', 'r')
str2 = f.readline() # 读取单独的一行
print(str2)
f.close()
print('---------------------')

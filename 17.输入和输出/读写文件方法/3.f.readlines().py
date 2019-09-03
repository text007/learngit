
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

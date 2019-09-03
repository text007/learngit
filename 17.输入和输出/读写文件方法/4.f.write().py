
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

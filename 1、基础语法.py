# 查看python保留关键字
import keyword
print(keyword.kwlist)
print('------------------------------')

# 注释
# 第一个注释
# 第二个注释
 
'''
第三注释
第四注释
'''
 
"""
第五注释
第六注释
"""
print ("Hello, Python!")
print('------------------------------')

# 行与缩进
if True:
    print ("True")
else:
    print ("False")
print('------------------------------')

# 多行语句
# total = item_one + \
#         item_two + \
#         item_three


# 数字(Number)类型
int     #(整数) 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool    #(布尔)如 True,False
float   #(浮点数)如 1.23、3E-2
complex #(复数)如 1 + 2j、 1.1 + 2.2j

# 字符串(String)
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
print('------------------------------')

# 字符串的截取:变量[头下标:尾下标:步长]
str='Runoob'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str * 2)             # 输出字符串两次
print(str + 'TEST')        # 连接字符串
 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
print('------------------------------')

# 等待用户输入
input("\n\n按下 enter 键后退出。")
print('------------------------------')

# 同一行显示多条语句
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
print('------------------------------')

# 多个语句构成代码组
if x : 
   pass
elif x : 
   pass 
else : 
   pass
print('------------------------------')

# Print 输出
x="a"
y="b"
# 换行输出
print( x )
print( y )
 
print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()
print('------------------------------')

# import 与 from...import
# 导入 sys 模块
import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

# 导入 sys 模块的 argv,path 成员
from sys import argv,path  #  导入特定的成员
 
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path
print('------------------------------')
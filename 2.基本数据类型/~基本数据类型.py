# 赋值
counter = 100
miles = 1000.0
name = "runoob"

print(counter)
print(miles)
print(name)
print('------------------------------')


# 多个变量赋值
a = b = c = 1
a, b, c = 1, 2, "runoob"
print('------------------------------')


# 标准数据类型
# Number      #（数字）
# String      #（字符串）
# List        #（列表）
# Tuple       #（元组）
# Set         #（集合）
# Dictionary  #（字典）

# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。


# Number（数字）  type() ：查询变量所指的对象类型
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

# isinstance来判断对象类型
a = 111
print(isinstance(a, int))

# isinstance与type区别
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
class A:
    pass

class B(A):
    pass

print(isinstance(A(),A))    #True
print(type(A()) == A)       #True
print(isinstance(B(),A))    #True
print(type(B()) == A)       #False
print('------------------------------')


# del删除元素
my_list = [1,2,3]
my_dict = {"name":"lowman", "age":12}
print('------------------------------')


del my_list[0]  #[0]指针位置
del my_dict["name"]
print(my_list)
print(my_dict)
print('------------------------------')


# 数值运算
print(5 + 4)    # 加法
print(4.3 - 2)  # 减法
print(3 * 7)    # 乘法
print(2 / 4)    # 除法，得到一个浮点数
print(2 // 4)   # 除法，得到一个整数
print(17 % 3)   # 取余 
print(2 ** 5)   # 乘方
print(2j + 3j)  # 复数运算；或者complex(a,b)表示，复数的实部a和虚部b都是浮点型
print('------------------------------')


# List（列表）
list1 = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist1 = [123, 'runoob']
 
print (list1)            # 输出完整列表
print (list1[0])         # 输出列表第一个元素
print (list1[1:3])       # 从第二个开始输出到第三个元素
print (list1[2:])        # 输出从第三个元素开始的所有元素
print (tinylist1 * 2)    # 输出两次列表
print (list1 + tinylist1) # 连接列表
print('------------------------------')


# List截取[头下标:尾下标:步长(-1 表示逆向)]
def reverseWords(input): 
      
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ") 
  
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],  
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样) 
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords=inputWords[-1::-1] 
  
    # 重新组合字符串
    output = ' '.join(inputWords) 
      
    return output 
  
if __name__ == "__main__": 
    input = 'I like runoob'
    rw = reverseWords(input) 
    print(rw)
print('------------------------------')


# Tuple（元组）
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')
 
print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
print('------------------------------')


# Set（集合）
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)

# 成员测试
if "Rose" in student:
    print("Rose 在集合中")

else :
    print("Rose 不在集合中")
print('------------------------------')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)    # a 和 b 的差集
print(a | b)    # a 和 b 的并集
print(a & b)    # a 和 b 的交集
print(a ^ b)    # a 和 b 中不同时存在的元素
print('------------------------------')

# Dictionary（字典）
dict = {}
dict['one'] = '1 - day1'
dict[2] = '2 - day2'

tinydict = {'name':'runoob', 'code':1, 'site':'www.123.com'}

print(dict['one'])          # 输出键为 'one' 的值
print(dict[2])              # 输出键为 2 的值
print(tinydict)             # 输出完整的字典
print(tinydict.keys())      # keys() 输出所有键
print(tinydict.values())    # values() 输出所有值
print('------------------------------')

# 字典遍历
print({x: x**2 for x in (2, 4, 6)})     #对x取值进行平方，再进行x的遍历
print('------------------------------')

# clear()方法
dicts = {'Name': 'Zara', 'Age': 7}
print(len(dicts))       #字典元素个数
dicts.clear()           #clear()删除字典内所有元素
print(len(dicts))       #字典元素个数
print('------------------------------')


# Python数据类型转换
'''
int(x [,base])          将x转换为一个整数
float(x)                将x转换到一个浮点数
complex(real [,imag])   创建一个复数
str(x)                  将对象 x 转换为字符串
repr(x)                 将对象 x 转换为表达式字符串
eval(str)               用来计算在字符串中的有效Python表达式,并返回一个对象
list(s)                 将序列 s 转换为一个列表
set(s)                  转换为可变集合
frozenset(s)            转换为不可变集合
chr(x)                  将一个整数转换为一个字符
ord(x)                  将一个字符转换为它的整数值
hex(x)                  将一个整数转换为一个十六进制字符串
oct(x)                  将一个整数转换为一个八进制字符串
'''

print(int(3.15))            #转换为整数
print(float(-10))           #转换为浮点数
print(complex(3.2 + -5))    #创建一个复数
print(str("3.33"))          #转换为字符串
print(repr("3.33"))         #转换为表达式字符串

aTuple = (123, 'Google', 'Runoob', 'Taobao')
list2 = list(aTuple)
print ("列表元素 : ", list2) #转换为列表

print(set('abcde'))         #转换为可变集合
print(frozenset(range(10))) #转换为不可变集合
print(chr(78))              #将整数转换为字符
print(ord('N'))             #将字符转换为整数
print(hex(255))             #转换为十六进制字符串
print(oct(255))             #转换为八进制字符串

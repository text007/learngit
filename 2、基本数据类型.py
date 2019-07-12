# 赋值
counter = 100
miles = 1000.0
name = "runoob"

print(counter)
print(miles)
print(name)


# 多个变量赋值
a = b = c = 1
a, b, c = 1, 2, "runoob"


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

# del删除元素
my_list = [1,2,3]
my_dict = {"name":"lowman", "age":12}

del my_list[0]  #[0]指针位置
del my_dict["name"]
print(my_list)
print(my_dict)


# 数值运算
print(5 + 4)    # 加法
print(4.3 - 2)  # 减法
print(3 * 7)    # 乘法
print(2 / 4)    # 除法，得到一个浮点数
print(2 // 4)   # 除法，得到一个整数
print(17 % 3)   # 取余 
print(2 ** 5)   # 乘方
print(2j + 3j)  # 复数运算；或者complex(a,b)表示，复数的实部a和虚部b都是浮点型


# List（列表）
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']
 
print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表

# List截取[头下标:尾下标:步长]
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


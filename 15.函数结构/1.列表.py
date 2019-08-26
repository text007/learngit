
# 列表
# 列表可以修改，而字符串和元组不能
# 列表的方法
'''
list.append(x)      把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
list.extend(L)      通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list.insert(i, x)	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
list.remove(x)      删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
list.pop([i])       从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
list.clear()        移除列表中的所有项，等于del a[:]。
list.index(x)       返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
list.count(x)       返回 x 在列表中出现的次数。
list.sort()         对列表中的元素进行排序。
list.reverse()      倒排列表中的元素。
list.copy()         返回列表的浅复制，等于a[:]。
'''
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))

a.insert(2, -1)
a.append(333)
print(a)

a.index(333)
print(a)
a.remove(333)
print(a)

a.reverse()
print(a)

a.sort()
print(a)
print('---------------------')

# 将列表当堆栈使用
# 列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）
# 用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来
stack = [3,4,5]
stack.append(6)     # 尾部添加元素
stack.append(7)
print(stack)

print(stack.pop())  # 移除尾部元素

print(stack.pop())

print(stack.pop())
print(stack)


# 将列表当队列使用
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")   # 尾部添加元素
queue.append("Graham")

print(queue.popleft())  # 移除头部元素

print(queue.popleft())

print(queue.popleft())
print(queue)
print('---------------------')

# 列表推导式
vec1 = [2,4,6]
print([3*x for x in vec1])
print([[x,x**2] for x in vec1])
print('---------------------')

vec2 = [2,4,6]
print([3*x for x in vec2 if x > 3]) # if 过滤器
print('---------------------')

fres = ['1d','a1','1c 1e1']
print([weapon.strip('1') for weapon in fres])   # strip() 移除头尾指定元素
print('---------------------')

vec3 = [2, 4, 6]
vec4 = [4, 3, -9]
print([x*y for x in vec3 for y in vec4])    # 每个元素相乘
print([x+y for x in vec3 for y in vec4])    # 每个元素相加
print([vec3[i]*vec4[i] for i in range(len(vec3))])    # 两个列表索引位置相乘
print('---------------------')

print([str(round(355/113, i)) for i in range(1, 6)])    # round（） 返回浮点数x的四舍五入值
print('---------------------')

# 嵌套列表解析
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
    ]

print([[row[i] for row in matrix] for i in range(4)])

# 方法2
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)

# 方法3
transposed2 = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed2.append(transposed_row)

print(transposed2)
print('---------------------')

# del语句
# 使用 del 语句可以从一个列表中依索引而不是值来删除一个元素
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]    # 删除单个元素
print(a)

del a[2:4]  # 删除部分元素
print(a)

del a[:]    # 删除所有元素
print(a)

del a       # 删除变量
# print(a)  # 报错

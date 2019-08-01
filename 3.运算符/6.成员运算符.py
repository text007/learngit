
# 成员运算符
'''
in	如果在指定的序列中找到值返回 True，否则返回 False。
not in	如果在指定的序列中没有找到值返回 True，否则返回 False。
'''

a = 10
b = 20
list1 = [1, 2, 3, 4, 5]

if (a in list1):
    print('a 在 list1 中')
else:
    print('a 不在 list1 中')

if (b not in list1):
    print("b 不在 list1 中")
else:
    print("b 在 list1 中")

# 修改变量 a 的值
a = 2
if (a in list1):
    print('a 在 list1 中')
else:
    print('a 不在 list1 中')

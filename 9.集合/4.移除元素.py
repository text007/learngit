
# 移除元素
# s.remove(x)
set7 = {'a', 'b', 1, 2, 'b', 2}
set7.remove(2)
print(set7)
# set7.remove('c')    # 元素不存在,返回错误
# print(set7)

# s.discard(x):元素不存在,不会报错
set7 = {'a', 'b', 1, 2, 'b', 2}
set7.discard('c')
print(set7)

# s.pop():随机删除一个元素
set8 = {'a', 'b', 1, 2, 'b', 2}
x = set8.pop()
print(set8)
print(x)

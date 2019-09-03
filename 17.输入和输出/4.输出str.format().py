
# str.format() 用法
print('数字：{}，字母：{}！'.format('123','abc'))

#括号中的数字用于指向传入对象在 format() 中的位置
print('{0} 和 {1}'.format('123', 'abc'))
print('{1} 和 {0}'.format('123', 'abc'))
print('---------------------')

# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数
print('数字：{name}，字母：{site}！'.format(name = '123', site = 'abc'))

# 位置及关键字参数可以任意的结合
print('{0}, {1}, 和 {other}'.format('123', 'abc',other = '!!!'))

# !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化
import math
print('pi≈ {!r}'.format(math.pi))
print('---------------------')

# 可选项 : 和格式标识符可以跟着字段名
print('pi≈ {0:.3f}'.format(math.pi))  # 0:.3f 保留3位小数

# 在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用
table = {'a':1,'b':2,'c':3}
for name, number in table.items():
    print('{0:5} ==> {1:5d}'.format(name,number))   # items() 函数以列表返回可遍历的(键, 值) 元组数组

print('---------------------')

# 格式化时通过变量名
# 使用方括号 [] 来访问键值
table1 = {'a':1,'b':2,'c':3}
print('a:{0[a]:d}; b:{0[b]:d}; c:{0[c]:d}'.format(table1))

# 通过在 table 变量前使用 ** 来实现相同的功能
table2 = {'a':1,'b':2,'c':3}
print('a:{a:d}; b:{b:d}; c:{c:d}'.format(**table2))
print('---------------------')

# 旧式字符串格式化
import math
print('pi≈ %5.3f。' % math.pi)  # 5位字符，3位小数
print('---------------------')

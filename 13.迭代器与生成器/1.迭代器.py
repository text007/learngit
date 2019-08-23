
# 迭代是Python最强大的功能之一，是访问集合元素的一种方式
# 迭代器是一个可以记住遍历的位置的对象
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退
# 迭代器有两个基本的方法：iter() 和 next()
# 字符串，列表或元组对象都可用于创建迭代器
list1 = [1,2,3,4]
it1 = iter(list1)
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
# print(next(it))   # 超过界限，抛出异常
print('--------------------')

# 迭代器对象可以使用常规for语句进行遍历
list2 = [1,2,3,4]
it2 = iter(list1)
for x in it2:
    print(x,end=' ')

print()
print('--------------------')

# 可以使用 next() 函数
import sys  # 引入 sys 模块

list3 = [1,2,3,4]
it3 = iter(list1)

while True:
    try:    # 判断下代码块是否异常，异常则执行except
        print(next(it3))
    except StopIteration:   # 异常来结束迭代
        sys.exit()

print('--------------------')

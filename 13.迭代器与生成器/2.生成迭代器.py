
# 创建一个迭代器
# 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 
# __iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成
# __next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象
class mynumbers:
    def __iter__(self):
        self.a = 1
        return self # 结束函数，返回一个值（默认返回None）

    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a += 1
            return x    # 结束函数，返回一个值（默认返回None）
        else:
            raise StopIteration # 异常来结束迭代

myclass = mynumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)


# 使用了 yield 的函数被称为生成器（generator）
# 生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器
# 遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行

# 使用 yield 实现斐波那契数列
import sys

def fib(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return  # 结束函数，返回一个值（默认返回None）
        yield a
        a, b = b, a+b
        counter += 1
f = fib(5)

while True:
    try:    # 判断下代码块是否异常，异常则执行except
        print(next(f),end=' ')
    except StopIteration:   # 异常来结束迭代
        sys.exit()

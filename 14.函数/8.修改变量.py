# global 和 nonlocal 关键字
# 修改全局变量
num = 1
def fun1():
    global num  # 声明修改全局变量
    print(num)
    num = 123
    print(num)
fun1()
print(num)
print('---------------')

# 修改嵌套作用域（enclosing 作用域，外层非全局作用域）
def outer():
    num = 10
    def inner():
        nonlocal num    # 声明修改局部变量
        num = 100
        print(num)
    inner()
    print(num)
outer()

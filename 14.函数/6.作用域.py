
# 变量作用域
# 程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的
'''
L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内置作用域（内置函数所在模块的范围）
只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问
'''
if True:
    msg = 'abc'
print(msg)

def test():
    msg_inner = 'ABC'
# print(msg_inner)  # 访问报错

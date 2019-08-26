
# return语句
# 退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None
def sum2(arg1, arg2):
    total = arg1 + arg2
    print('内：', total)
    return total    # 返回 total 的值

total = sum2(10, 20)
print('外：', total)

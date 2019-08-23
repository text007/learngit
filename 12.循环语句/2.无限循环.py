
# 通过设置条件表达式永远不为 false 来实现无限循环
# 无限循环在服务器上客户端的实时请求非常有用
var = 1
while var == 1:
    num = int(input('数字：'))
    print(num)

print('跳出')
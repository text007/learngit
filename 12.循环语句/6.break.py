
# break 语句可以跳出 for 和 while 的循环体。
# 如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行
for letter in 'abcde':
    if letter == 'd':   # 当 letter 等于 d
        break           # 结束循环
    print('当前字母：', letter)

print('--------------------')

var = 10
while var > 0:
    print(var)
    var -= 1
    if var == 5:
        break

print('跳出')
print('--------------------')

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n,'等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素:n 除以 x 的各个元素不等于0
        print(n, '是质数')

# 运行过程
'''
n   x               n//x
2                                               x没有元素
3   2               3/2                         不整除
4   2,3             4/2,4/3                     整除（4/2）
5   2,3,4           5/2,5/3,5/4                 不整除
6   2,3,4,5         6/2,6/3,6/4,6/5             整除（6/2）
7   2,3,4,5,6       7/2,7/3,7/4,7/5,7/6         不整除
8   2,3,4,5,6,7     8/2,8/3,8/4,8/5,8/6,8/7     整除（8/2）
9   2,3,4,5,6,7,8   9/2,9/3,9/4,9/5,9/6,9/7,9/8 整除（9/3）
'''
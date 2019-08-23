
# if中常用的操作运算符
'''
<	小于
<=	小于或等于
>	大于
>=	大于或等于
==	等于，比较两个值是否相等
!=	不等于
'''
number = 7
guess = -1
print('数字猜谜游戏！')
while guess != number:
    guess = int(input('请输入你猜的数字：'))

    if guess ==number:
        print('答对啦')
    elif guess < number:
        print('小啦')
    elif guess > number:
        print('大啦')
        
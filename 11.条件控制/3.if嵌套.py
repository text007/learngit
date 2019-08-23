
num = int(input('输入一个数字：'))
if num%2 == 0:
    if num%3 == 0:
        print('整除2和3')
    else:
        print('整除2，不能整除3')
else:
    if num%3 == 0:
        print('整除3，不能整除2')
    else:
        print('不能整除2和3')
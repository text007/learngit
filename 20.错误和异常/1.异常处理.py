
# 处理 ZeroDivisionError 异常
# 使用try - except 处理异常
try:
    print(5/0)
except ZeroDivisionError:
    print('不能除以0')

# try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。
# 这个子句将在try子句没有发生任何异常的时候执行
while True:
    first_number = input('First number:')
    if first_number == 'q': # 当输入q
        break   # 退出
    second_number = input('Second number:')
    if second_number == 'q':    # 当输入q
        break   # 退出
    try:
        answer = int(first_number) / int(second_number) # 求商
    except ZeroDivisionError:
        print('不能除以0')
    else:   # try 无异常将执行
        print(answer)


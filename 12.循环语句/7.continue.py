
# continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环
for letter in 'abcdde':
    if letter == 'd':   # 当 letter 等于 d
        continue        # 跳出当前循环，进入下个循环
    print('当前字母:', letter)

var = 10
while var > 0:
    var -= 1
    if var == 5:
        continue
    print('当前变量：', var)
print('跳出')

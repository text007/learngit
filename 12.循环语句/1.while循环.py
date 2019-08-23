
n = 100     # 定义初始值
sum1 = 0
counter = 1
while counter <= n:
    sum1 += counter # sum1 = sum1 + counter
    counter +=1     # counter = counter + 1

print('1 到 %d 之和为：%d' %(n,sum1))

# 符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格
for x in range(1,11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=" ")
    print(repr(x*x*x).rjust(5))
    
print('---------------------')

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)) # 2d 两个空格

print('---------------------')

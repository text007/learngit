
# for循环可以遍历任何序列的项目，如一个列表或者一个字符串
languages = {'C', 'C++', 'python', 'php'}
for x in languages:
    print(x)

print('------------------------------')

# break 语句用于跳出当前循环体
sites = ['1', '2', 3, 4]
for sites in sites:
    if sites == 3:
        print('跳出')
        break           # break 语句用于跳出当前循环体
    print(sites)
else:
    print('无数据')
print('结束')

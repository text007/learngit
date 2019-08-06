
# find()方法：检测字符串中是否包含子字符串,包含返回索引位置，不包含返回-1
str7 = 'Runoob example....wow!!!'
str8 = 'exa'

print(str7.find(str8,5))    #5起始，包含返回索引位置
print(str7.find(str8,10))   #10起始，不包含返回-1


# rfind()方法：返回字符串最后一次出现的位置，如果没有匹配项则返回-1
# find()方法：返回字符串第一次出现的位置，如果没有匹配项则返回-1
str34 = "this is string example....this is...!!!"
str35 = 'is'
print(str34.rfind(str35, 0, 10))
print(str34.rfind(str35, 10, 0))
print(str34.find(str35, 0, 10))
print(str34.find(str35, 10, 0))

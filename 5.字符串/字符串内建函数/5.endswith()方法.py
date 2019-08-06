
# endswith()方法：判断字符串是否以指定后缀结尾
str5= 'Runoob example....wow!!!'
suffix1= '!!'
print(str5.endswith(suffix1,16))        #开始位置16
suffix2= 'w'
print(str5.endswith(suffix2, 0, 25))    #0开始，25结束


# splitlines()方法：按照行('\r','\r\n',\n')分隔，返回一个包含各行作为元素的列表，如果参数keepends为False，不包含换行符，如果为True，则保留换行符
str41 = 'ad c\n\nde fg\r\n'
print(str41.splitlines())
print(str41.splitlines(True))

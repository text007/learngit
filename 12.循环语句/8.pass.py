
# pass是空语句，是为了保持程序结构的完整性，属于占位字符
for letter in 'abcdde': 
   if letter == 'd':
      pass
      print ('执行 pass 块')
   print ('当前字母 :', letter)
 
print ("结束")
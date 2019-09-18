
# os.chdir() 方法用于改变当前工作目录到指定的路径
import os, sys
path = 'D:/learngit/18.file'
retval = os.getcwd()
print('当前目录 %s'% retval)

os.chdir(path)
retval1 = os.getcwd()
print('修改后目录 %s'% retval1)
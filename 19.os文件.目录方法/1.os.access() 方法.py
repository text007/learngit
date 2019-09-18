
# os.access() 方法使用当前的uid/gid尝试访问路径
# os.access(path, mode)
# path -- 要用来检测是否有访问权限的路径。
# mode -- mode为F_OK，测试存在的路径，或者它可以是包含R_OK, W_OK和X_OK或者R_OK, W_OK和X_OK其中之一或者更多。
    # os.F_OK: 作为access()的mode参数，测试path是否存在。
    # os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读。
    # os.W_OK 包含在access()的mode参数中 ， 测试path是否可写。
    # os.X_OK 包含在access()的mode参数中 ，测试path是否可执行。

import os, sys

ret1 = os.access('test.txt', os.F_OK)
print('F_OK - 返回值 %s' % ret1)

ret2 = os.access('test.txt', os.R_OK)
print('R_OK - 返回值 %s' % ret2)

ret3 = os.access('test.txt', os.W_OK)
print('W_OK - 返回值 %s' % ret3)

ret4 = os.access('test.txt', os.X_OK)
print('X_OK - 返回值 %s' % ret4)

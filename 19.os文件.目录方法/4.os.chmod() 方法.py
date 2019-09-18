
# os.chmod() 方法用于更改文件或目录的权限
# os.chmod(path, mode)
# path -- 文件名路径或目录路径。
# flags -- 可用以下选项按位或操作生成， 目录的读权限表示可以获取目录里文件名列表， ，执行权限表示可以把工作目录切换到此目录 ，删除添加目录里的文件必须同时有写和执行权限 ，文件权限以用户id->组id->其它顺序检验,最先匹配的允许或禁止权限被应用。
#     stat.S_IXOTH: 其他用户有执行权0o001
#     stat.S_IWOTH: 其他用户有写权限0o002
#     stat.S_IROTH: 其他用户有读权限0o004
#     stat.S_IRWXO: 其他用户有全部权限(权限掩码)0o007
#     stat.S_IXGRP: 组用户有执行权限0o010
#     stat.S_IWGRP: 组用户有写权限0o020
#     stat.S_IRGRP: 组用户有读权限0o040
#     stat.S_IRWXG: 组用户有全部权限(权限掩码)0o070
#     stat.S_IXUSR: 拥有者具有执行权限0o100
#     stat.S_IWUSR: 拥有者具有写权限0o200
#     stat.S_IRUSR: 拥有者具有读权限0o400
#     stat.S_IRWXU: 拥有者有全部权限(权限掩码)0o700
#     stat.S_ISVTX: 目录里文件目录只有拥有者才可删除更改0o1000
#     stat.S_ISGID: 执行此文件其进程有效组为文件所在组0o2000
#     stat.S_ISUID: 执行此文件其进程有效用户为文件所有者0o4000
#     stat.S_IREAD: windows下设为只读
#     stat.S_IWRITE: windows下取消只读

import os, sys, stat
os.chmod('D:/learngit/19.os文件.目录方法/test.txt', stat.S_IXGRP)
os.chmod('D:/learngit/19.os文件.目录方法/test.txt', stat.S_IWOTH)
print('11')
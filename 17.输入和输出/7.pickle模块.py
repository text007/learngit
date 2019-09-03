
# pickle 模块
# 实现基本的数据序列和反序列化
# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象
import pickle   # 导入模块
data1 = {'a':[1, 2.0, 3, 4+6j], # 创建一个字典
    'b':('s',u'Un'),
    'c':None}

s_l = [1, 2, 3] # 创建一个列表
s_l.append(s_l)     # 列表末尾添加一个列表

o = open('data.pk1', 'wb')  # 打开一个文件（没有就创建），读取写入

pickle.dump(data1, o)   # 用pickle模块使字典保存到文件中
pickle.dump(s_l, o, -1) # 用pickle模块使列表保存到文件中
o.close()   # 关闭文件

# load() 反序列化对象，将文件中的数据解析为一个python对象
import pprint, pickle  # 导入模块
p_f = open('data.pk1', 'rb')    # 打开文件
data2 = pickle.load(p_f)    # 反序列化文件对象
pprint.pprint(data2)    # 美化格式

data3 = pickle.load(p_f)    # 反序列化文件对象
pprint.pprint(data3)    # 美化格式

p_f.close() # 关闭文件

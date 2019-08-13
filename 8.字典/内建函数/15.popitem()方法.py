
# popitem()方法:随机返回并删除字典中的一对键和值(一般删除末尾对)
# 如果字典已经为空，却调用了此方法，就报出KeyError异常
dict23 = {'a':'1','b':'2'}
pop_obj = dict23.popitem()
print(pop_obj)  # 返回已删除的值
print(dict23)

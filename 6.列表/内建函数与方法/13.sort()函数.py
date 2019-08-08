
# sort()函数:用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数
# reverse = True 降序， reverse = False 升序（默认）
def takesecond(elem):           # 获取列表中元组的第二个元素
    return elem[1]

random = [(2,2), (3,4), (4,1), (1,3)]
random.sort(key = takesecond)   # 指定第二个元素排序
print(random)

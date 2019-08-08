
# extend()函数:用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list8 = [123, 'abc', 123]
list9 = list(range(5))      # 创建 0-4 的列表
list8.extend(list9)         # 扩展列表
print(list8)

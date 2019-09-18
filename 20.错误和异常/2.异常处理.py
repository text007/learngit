
# 处理 FileNotFoundError 异常
# 找不到要打开的文件时创建的异常

def count_words(filename):
# '''文件包含多少个单词'''
    try:
        with open(filename) as f_obj:   # 打开文件
            contents = f_obj.read() # 读取文件内容
    except FileNotFoundError:   # 异常时
        print("文件" + filename + "不存在") # 异常处理；pass时将不显示异常处理，继续运行
    else:
        words = contents.split()    # 生产一个列表包含所有内容
        num_words = len(words)  # 确认列表长度
        print('文件大于有' + str(num_words) + '单词')

filenames = ['alice.txt', 'a1.txt', 'a2.txt', 'a3.txt']
for filename in filenames:
    count_words(filename)

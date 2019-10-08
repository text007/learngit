'''需要测试的方法'''
def get_formatted_name(first, last, middle=''):    # 定义一个函数，传入两个参数
    if middle:
        full_name = first + ' ' + middle + ' ' + last    # 合并两个参数
    else:
        full_name = first + ' ' + last
    return full_name.title()    # 返回合并的结果

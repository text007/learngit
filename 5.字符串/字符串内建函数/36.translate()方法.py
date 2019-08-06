
# translate()方法:根据参数table给出的表(包含256个字符)转换字符串的字符,要过滤掉的字符放到deletechars参数中
# 制作翻译表：maketrans（）方法：b1与b2一一对应，相互转换; bytes()方法：创建字符节码
bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(b'abcdoob'.translate(bytes_tabtrans, b'o'))   # 转换为大写，并删除字母

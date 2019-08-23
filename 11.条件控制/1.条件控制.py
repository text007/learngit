
# 条件语句
# if 语句
age = int(input('请输入你家狗狗的年龄：'))
if age <= 0:
    print('你是在逗我吧!')
elif age == 1:
    print('相当于人类14岁。')
elif age == 2:
    print('相当于人类22岁。')
elif age > 2:
    human = 22 +(age -2)*5
    print('对应人类年龄：', human)

input('点击 enter 键退出')

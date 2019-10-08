'''需要测试类'''
class AnonymousSurvey():    # 定义一个类
    '''收集匿名调查问卷的答案'''

    def __init__(self, question):
        # __init__ 特殊方法：创建新实例时python都会运行，避免默认方法与普通方法冲突
        '''存储一个问题，并为存储答案做准备'''
        self.question = question    # 初始化属性，并保存
        self.responses = [] # 创建一个空列表，为存储答案做准备

    def show_question(self):    # 定义一个方法
        '''显示调查问卷'''
        print(self.question)    # 打印显示问题

    def store_response(self, new_response): # 定义一个方法
        '''存储单份调查卷'''
        self.responses.append(new_response) # 存储答案到列表中

    def show_results(self): # 定义一个方法
        '''显示收集到的所有答案'''
        print('Survey results:')    # 打印提示语
        for response in self.responses: # （self.responses）列表中的答案分别赋值给response
            print('- ' + response)  # 打印使用答案

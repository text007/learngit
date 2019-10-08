'''测试类'''
import unittest # 调用方法
from survey import AnonymousSurvey  # 调用方法

class TestAnonymousSurvey(unittest.TestCase):   # 定义一个类
    '''针对类的测试'''

    def setUp(self):
        '''如果在 unittest.TestCase 类中包含 setUp（）方法 ，python将先运行它，在运行各个test_打头的方法'''
        '''创建一个问题和一组答案，供测试方法使用'''
        question = 'What language did you first learn to speak?'    # 把问题赋值给 question
        self.my_survey = AnonymousSurvey(question)  # 创建一个实例，把问题传入需测试的类(AnonymousSurvey)中，并把结果赋值给my_survey
        self.responses = ['English', 'Spanish', 'Mandarin'] #创建一个答案列表


    def test_store_single_response(self):   # 定义一个方法
        '''测试单个答案会被存储'''
        self.my_survey.store_response(self.responses[0])    # 把答案列表第一个参数传入方法 store_response 中，并把结果赋值给 self.my_survey
        self.assertIn(self.responses[0],self.my_survey.responses)   # 调用方法断言答案在列表中第一个参数
   
    def test_store_three_responses(self):   # 定义一个方法
        '''测试三个答案会被存储'''
        for response in self.responses:  # 把列表中每个值分别赋值给response
            self.my_survey.store_response(response)  # 把列表中每个答案分别传入（store_response）方法中

        for response in self.responses:  # 把列表中每个值分别赋值给response
            self.assertIn(response, self.my_survey.responses)    # 调用方法断言答案在列表中

unittest.main()

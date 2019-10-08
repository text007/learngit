'''单元测试'''
import unittest # 调用方法
from name_function import get_formatted_name    # 调用方法

class NamesTestCase(unittest.TestCase): # 定义一个类

    def test_first_last_name(self): # 定义一个方法，传入一个参数
        formatted_name = get_formatted_name('janis', 'joplin')  # 给测试函数传入两个参数，结果保存到函数中
        self.assertEqual(formatted_name, 'Janis Joplin') # 调用测试函数，断言结果与预期结果相同

    def test_first_last_middle_name(self):  # 定义一个方法，传入一个参数
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')    # 给测试函数传入三个参数，结果保存到函数中
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart') # 调用测试函数，断言结果与预期结果相同

unittest.main() # 运行改方法

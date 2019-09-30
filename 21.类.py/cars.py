
'''一个类'''
class Car():    # 定义一个类

    def __init__(self, make, model, year):
        self.make = make    # 初始化属性，并保存
        self.model = model
        self.year = year
        self.odometer_reading = 5   # 给属性指定默认值

    def get(self):
        long_name = str(self.year) + ' ' + self.model + ' ' + self.make
        return long_name.title()    # 返回参数属性

    def read_odometer(self):
        print(str(self.odometer_reading))

    def update_odometer(self, mileage): # 传入两个参数
        if mileage >= self.odometer_reading:    # 判断条件
            self.odometer_reading = mileage # 想属性值存储到函数中
        else:
            print('不能小于初始值。')

    def increment_odometer(self, miles):
        self.odometer_reading += miles

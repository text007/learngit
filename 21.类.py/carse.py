
'''一个类'''

# 导入另外一个类
from cars import Car
class Battery():    # 定义一个类

    def __init__(self, battery_size = 70):  # 定义一个方法，传入一个形参，如果没有传入参数值，则默认值
        self.battery_size = battery_size    # 初始化

    def describe_battery(self): # 定义一个方法
        print(str(self.battery_size))   # 打印

    def get_range(self):    # 定义一个方法
        if self.battery_size == 70: # 当
            range = 240 
        elif self.battery_size == 85:   # 当
            range = 270

        message = 'T ' + str(range)
        message += ' m'
        print(message)  # 打印


class ElectricCar(Car): # 定义子类，（）中必须包含父类名称

    def __init__(self, make, model, year):  # 接受创建父类实例所需信息
        # 初始化父类属性
        # super()：特殊方法；将父类与子类关联
        super().__init__(make, model, year)
        self.battery = Battery()  # 子类包含这个属性，父类不包含
        
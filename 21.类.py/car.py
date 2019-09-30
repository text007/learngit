
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
        
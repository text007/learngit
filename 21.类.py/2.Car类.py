
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

my_new_car = Car('sunbaru', 'outback', 2016)    # 创建实例，传入参数属性，保存在变量中
print(my_new_car.get())

# 调用方法，并提供一个实参
my_new_car.update_odometer(23500)  # 通过方法修改属性的值
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
# my_new_car.odometer_reading = 23    # 通过实例直接访问参数并修改
my_new_car.read_odometer()  # 在类中查找该方法，并执行

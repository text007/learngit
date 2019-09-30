
# 导入文件的类
from car import Car

my_new_car = Car('sunbaru', 'outback', 2016)    # 创建实例，传入参数属性，保存在变量中
print(my_new_car.get())

my_new_car.odometer_reading = 23    # 通过实例直接访问参数并修改
my_new_car.read_odometer()  # 在类中查找该方法，并执行
print('1---------')


# 导入文件的类
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)    # 创建实例
print(my_tesla.get())   # 打印方法

my_tesla.battery.describe_battery() # 调用
my_tesla.battery.get_range()    # 调用
print('2---------')


# 导入文件的多个类
from car import Car, ElectricCar 

my_new_car = Car('sunbaru', 'outback', 2016)    # 创建实例，传入参数属性，保存在变量中
print(my_new_car.get())

my_tesla = ElectricCar('tesla', 'model s', 2016)    # 创建实例
print(my_tesla.get())   # 打印方法
print('3---------')


# 导入所有类
from car import *

my_beetle = Car('sunbaru', 'outback', 2016)
print(my_new_car.get())

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get())
print('4---------')


# 导入整个模块
import car

# 句点表示法访问需要的类
my_beetle = car.Car('sunbaru', 'outback', 2016)
print(my_new_car.get())

my_tesla = car.ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get())
print('5---------')

# 访问两个不同模块
from cars import Car
from carse import ElectricCar

my_beetle = Car('sunbaru', 'outback', 2016)
print(my_new_car.get())

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get())

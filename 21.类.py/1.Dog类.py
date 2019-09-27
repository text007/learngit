
# 面向对象技术简介
# 类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
# 方法：类中定义的函数。
# 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
# 数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
# 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
# 局部变量：定义在方法中的变量，只作用于当前实例的类。
# 实例变量：在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
# 继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
# 实例化：创建一个类的实例，类的具体对象。
# 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法

# 创建dog类
class Dog():    # 定义一个 Dog 类（python规定首字母大写的名称指的是类）

    def __init__(self, name, age):  # 包含三个形参
        # __init__ 特殊方法：创建新实例时python都会运行，避免默认方法与普通方法冲突
        self.name = name    # 初始化属性name，age 并保存
        self.age = age

    def sit(self):
        print(self.name.title() + '蹲下')

    def roll_over(self):
        print(self.name.title() + '打滚')

my_dog = Dog('willie', 6)   # 小写名称是根据类型创建的实例
your_dog = Dog('luck', 3)

print(my_dog.name.title())
print(str(my_dog.age))

my_dog.sit()    # 在类中查找sit方法，并执行
print(your_dog.name.title())
print(str(your_dog.age))
my_dog.roll_over()


# import 语句
import fibo     # 导入自定义的 fibo 模块(F:\python3.7.3\fibo.py)
print(fibo.fib(1000))
print(fibo.fib2(50))
print(fibo.__name__)
print('---------------------')
# from ... import * 语句
# 导入一个模块中的所有项目

from fibo import fib, fib2
print(fib(500))
print('---------------------')

# __name__属性
# 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入

# dir() 函数
# 找到模块内定义的所有名称
# 如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称
import fibo, sys
print(dir(fibo))
print(dir(sys))
print('---------------------')


# 标准模块
# Python 本身带着一些标准的模块库
# 有些模块直接被构建在解析器里，这些虽然不是一些语言内置的功能，但是他却能很高效的使用，甚至是系统级调用也没问题
# 这些组件会根据不同的操作系统进行不同形式的配置，比如 winreg 这个模块就只会提供给 Windows 系统
# 特别的模块 sys ，它内置在每一个 Python 解析器中。变量 sys.ps1 和 sys.ps2 定义了主提示符和副提示符所对应的字符串

# 包
# 包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
# 比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B 。
# 就好像使用模块的时候，你不用担心不同模块之间的全局变量相互影响一样，采用点模块名称这种形式也不用担心不同库之间的模块重名的情况。
# 这样不同的作者都可以提供 NumPy 模块，或者是 Python 图形库。
# 不妨假设你想设计一套统一处理声音文件和数据的模块（或者称之为一个"包"）。
# 现存很多种不同的音频文件格式（基本上都是通过后缀名区分的，例如： .wav，:file:.aiff，:file:.au，），所以你需要有一组不断增加的模块，用来在不同的格式之间转换。
# 并且针对这些音频数据，还有很多不同的操作（比如混音，添加回声，增加均衡器功能，创建人造立体声效果），所以你还需要一组怎么也写不完的模块来处理这些操作
# 在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录。
# 目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。
# 最简单的情况，放一个空的 :file:__init__.py就可以了。当然这个文件中也可以包含一些初始化代码或者为（将在后面介绍的） __all__变量赋值。
# 用户可以每次只导入一个包里面的特定模块：
# import sound.effects.echo
# 这将会导入子模块:sound.effects.echo。 他必须使用全名去访问:
# sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

# 还有一种导入子模块的方法是:
# from sound.effects import echo
# 这同样会导入子模块: echo，并且他不需要那些冗长的前缀，所以他可以这样使用:
# echo.echofilter(input, output, delay=0.7, atten=4)

# 还有一种变化就是直接导入一个函数或者变量:
# from sound.effects.echo import echofilter
# 这种方法会导入子模块: echo，并且可以直接使用他的 echofilter() 函数:
# echofilter(input, output, delay=0.7, atten=4)

# 注意当使用from package import item这种形式的时候，对应的item既可以是包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量。
# import语法会首先把item当作一个包定义的名称，如果没找到，再试图按照一个模块去导入。如果还没找到，恭喜，一个:exc:ImportError 异常被抛出了。
# 反之，如果使用形如import item.subitem.subsubitem这种导入形式，除了最后一项，都必须是包，而最后一项则可以是模块或者是包，但是不可以是类，函数或者变量的名字

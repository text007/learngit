
# difference_update()方法：用于移除两个集合中都存在的元素
# ifference_update() 方法与 difference() 方法的区别在于 difference() 方法返回一个移除相同元素的新集合，
# 而 difference_update() 方法是直接在原来的集合中移除元素，没有返回值。
set18 = {'a', 'b', 1, 2}
set19 = {'a', 'c', 3, 2}
set18.difference_update(set19)
print(set18)

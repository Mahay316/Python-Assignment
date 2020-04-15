# 练习: 定义类，使用类变量和实例变量，定义实例方法
class Dog:
    count = 0

    def __init__(self, name, color):
        self.name = name
        self.color = color
        Dog.count += 1

    def bark(self):
        print('{0}: woof!'.format(self.name))


d1 = Dog('dog1', 'Orange')
d1.bark()
d2 = Dog('dog2', 'Gray')
d2.bark()
print(Dog.count)

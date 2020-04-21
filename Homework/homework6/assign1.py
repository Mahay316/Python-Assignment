# 1. 定义一个狗类，里面有一个列表成员变量（列表的元素是字典）
# 分别记录了3种颜色的狗的颜色、数量和价格
# 实现狗的买卖交易方法
# 打印输出经过2-3次买卖方法后，剩下的各类狗的数量


class Dog:
    # 狗的颜色的常量
    COLOR_BLACK = 'black'
    COLOR_ORANGE = 'orange'
    COLOR_WHITE = 'white'

    def __init__(self):
        self.dog_list = [
            {'color': Dog.COLOR_BLACK, 'num': 5, 'price': 1000},
            {'color': Dog.COLOR_ORANGE, 'num': 8, 'price': 800},
            {'color': Dog.COLOR_WHITE, 'num': 3, 'price': 900}
        ]

    def buy(self, color, num):
        '''买入狗，调用后对应颜色狗的数量增加'''
        if not isinstance(num, int):
            raise TypeError('狗的数量必须为整数')
        if num <= 0:
            raise ValueError('狗的数量必须为正整数')

        for d in self.dog_list:
            if d['color'] == color:
                d['num'] += num
                print(f'买入{num}只{color}颜色的狗, 剩余{d["num"]}只')
                break
        else:
            print(f'不存在{color}颜色的狗')

    def sell(self, color, num):
        '''卖出狗，调用后对应颜色狗的数量减少'''
        if not isinstance(num, int):
            raise TypeError('狗的数量必须为整数')
        if num <= 0:
            raise ValueError('狗的数量必须为正整数')

        for d in self.dog_list:
            if d['color'] == color:
                if d['num'] >= num:
                    d['num'] -= num
                    print(f'售出{num}只{color}颜色的狗, 剩余{d["num"]}只')
                else:
                    print(f'狗的数量不足{num}只, 交易取消')
                break
        else:
            print(f'不存在{color}颜色的狗')

    def show(self):
        print(' 颜色   数量     价格')
        for d in self.dog_list:
            print("%-6s  %2d    ￥%6.2f" % (d['color'], d['num'], d['price']))
        print()


if __name__ == '__main__':
    dog = Dog()
    print('交易前狗的数量:')
    dog.show()

    dog.sell(Dog.COLOR_BLACK, 2)
    dog.buy(Dog.COLOR_ORANGE, 6)
    dog.sell(Dog.COLOR_WHITE, 1)

    print('\n交易后狗的数量:')
    dog.show()

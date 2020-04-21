# 游戏规则：
# A 游戏开始后，生成2个人，3条狗，人狗互相交替对战（人只能打狗，狗也只会咬人）
# B 血为0的话，表示死亡，退出游戏
# C 人和狗的攻击力，都会因为被咬或被打而降低(人被咬一次降低2；狗被打一次降低3)
# D 任意一方所有角色全部死亡认定为负，另一方认定为胜
#
# 对战规则：
# A 随机决定，谁先开始攻击
# B 一方攻击完毕后，另外一方再开始攻击，攻击的目标是随机的
# C 每次攻击，双方只能安排一个人，或者一条狗进行攻击
from random import randint
from dog import Dog
from human import Human
from time import sleep


class Fight:
    '''处理人狗对战逻辑，并输出对战信息'''
    def __init__(self, p=2, d=3):
        # 生成p个人，d条狗
        self.people = []
        for i in range(1, p + 1):
            self.people.append(Human(i))
        self.dogs = []
        for i in range(1, d + 1):
            self.dogs.append(Dog(i))
        # 随机决定比赛顺序
        self.human_first = bool(randint(0, 1))

    # private method
    def __human2dog(self):
        # 随机选一个人，随机攻击一条狗
        man = randint(0, len(self.people) - 1)
        dog = randint(0, len(self.dogs) - 1)
        # 掉血
        self.dogs[dog].hp -= self.people[man].atk
        # 掉攻击力，攻击方攻击力为0则不减被攻击方攻击力
        self.dogs[dog].atk -= (self.people[man].atk > 0) * 3

        print(f'人{self.people[man].no}攻击了狗{self.dogs[dog].no}，', end='')
        print(f'hp -{self.people[man].atk}，狗{self.dogs[dog].no}', end='')
        print(f'剩余血量{self.dogs[dog].hp}')
        # 去除血量为0的个体
        if self.dogs[dog].is_dead():
            print(f'狗{self.dogs[dog].no}死亡')
            del self.dogs[dog]

    # private method
    def __dog2human(self):
        # 随机选一只狗，随机攻击一个人
        dog = randint(0, len(self.dogs) - 1)
        man = randint(0, len(self.people) - 1)
        # 掉血
        self.people[man].hp -= self.dogs[dog].atk
        # 掉攻击力
        self.people[man].atk -= (self.dogs[dog].atk > 0) * 2

        print(f'狗{self.dogs[dog].no}攻击了人{self.people[man].no}，', end='')
        print(f'hp -{self.dogs[dog].atk}，人{self.people[man].no}', end='')
        print(f'剩余血量{self.people[man].hp}')
        # 去除血量为0的个体
        if self.people[man].is_dead():
            print(f'人{self.people[man].no}死亡')
            del self.people[man]

    def round(self):
        '''进行一回合比赛'''
        if self.human_first:
            self.__human2dog()
            if self.__result():
                # 胜负已经决出
                return
            self.__dog2human()
        else:
            self.__dog2human()
            if self.__result():
                # 胜负已经决出
                return
            self.__human2dog()

    # private method
    def __result(self):
        '''返回比赛结果
            人胜返回1
            狗胜返回2
            未定胜负返回0
        '''
        if len(self.dogs) == 0:
            return 1
        elif len(self.people) == 0:
            return 2

        return 0

    def fight(self):
        '''开始对战，输出实时对战结果，并显示胜负'''
        # 还未分出胜负就继续比赛
        i = 1
        while not self.__result():
            print(f"-------- ROUND {i} --------")
            self.round()
            i += 1
            sleep(0.5)

        print('\n 胜负决出，%s！' % ('人胜' if self.__result() == 1 else '狗胜'))


if __name__ == '__main__':
    f = Fight()
    f.fight()

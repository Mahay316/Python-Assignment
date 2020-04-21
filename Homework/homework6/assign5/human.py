# 人的初始攻击力为10，初始化血为100
# 血为0的话，表示死亡，退出游戏
# 人的攻击力，会因为被咬而降低（人被咬一次，攻击力降低2）


class Human():
    def __init__(self, no, hp=100, atk=10):
        self._no = no
        # 初始化人类的血量和攻击力
        self._hp = hp
        self._atk = atk

    @property
    def no(self):
        # 编号为只读属性
        return self._no

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        if value <= 0:
            self._hp = 0
        else:
            self._hp = value

    @property
    def atk(self):
        return self._atk

    @atk.setter
    def atk(self, value):
        if value <= 0:
            self._atk = 0
        else:
            self._atk = value

    def is_dead(self):
        '''血量为0认为角色死亡'''
        return self.hp == 0

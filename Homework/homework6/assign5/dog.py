# 狗的攻击力为15，初始化血为80
# 血为0的话，表示死亡，退出游戏
# 狗的攻击力，会因为被打而降低（狗被打一次，攻击力降低3）


class Dog():
    def __init__(self, no, hp=80, atk=15):
        self._no = no
        # 初始化狗的血量和攻击力
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
        return self.hp <= 0

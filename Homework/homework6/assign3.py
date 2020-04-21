# 3. 定义一个字典类：dictclass，完成下面的功能：
#   dict = dictclass({你需要操作的字典对象})
# 删除某个key
#   del_dict(key)
# 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
#   get_dict(key)
# 返回键组成的列表
#   get_key() -> list
# 合并字典，并且返回合并后字典的value组成的列表
#   update_dict({要合并的字典}) -> list


class dictclass:
    '''封装了对字典的一些常用操作'''
    def __init__(self, target):
        if isinstance(target, dict):
            self.target = target
        else:
            # 默认创建一个空的字典
            self.target = {}

    def del_dict(self, key):
        '''删除字典中key对应的元素
        返回删除的value，未找到返回None
        '''
        val = None
        if key in self.target:
            val = self.target[key]
            del self.target[key]

        return val

    def get_dict(self, key):
        '''判断key是否是字典的键'''
        if key in self.target:
            return self.target[key]
        else:
            return 'not found'

    def get_key(self):
        return list(self.target.keys())

    def update_dict(self, other):
        if not isinstance(other, dict):
            raise TypeError('合并的必须是一个字典')

        self.target.update(other)
        return list(self.target.values())


if __name__ == '__main__':
    test = {'color': 'blue', 'age': 25, 'score': 145}
    dic = dictclass(test)

    print(dic.get_key())
    print('删除键color，其对应值为:', dic.del_dict('color'))
    print(dic.get_key())

    more = {'money': 50, 1: 'number'}
    print('合并字典，合并后的所有value:', dic.update_dict(more))

    print('搜索键test:', dic.get_dict('test'))
    print('搜索键money:', dic.get_dict('money'))

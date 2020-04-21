# 6. 用面向对象，实现一个学生Python成绩管理系统
# 学生的信息存储在文件中
# 学生信息的字段有(班级、学号、姓名、Python成绩)
# 实现对学生信息及成绩的增、删、改、查方法


class Student:
    '''学生类
    保存学生的基本信息：学号，班级，姓名，成绩
    '''
    def __init__(self, no, clz, name, score):
        self._no = no
        self.clz = clz
        self.name = name
        if not isinstance(score, int) or score < 0 or score > 100:
            # 参数不合法，将score设为默认值
            self._score = 0
        else:
            self._score = score

    def __str__(self):
        '''用于将Student对象转换成字符串'''
        return "%s %s %s %s" % (self._no, self.clz, self.name, self._score)

    @property
    def no(self):
        # 学号no为只读属性
        return self._no

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('成绩必须是整型数据')
        elif value < 0 or value > 100:
            raise ValueError('成绩应在0到100之间')
        self._score = value

    def writeToFile(self, f):
        '''将Student对象信息写入文件'''
        f.write(self.__str__())
        f.write('\n')

# 6. 用面向对象，实现一个学生Python成绩管理系统
# 学生的信息存储在文件中
# 学生信息的字段有(班级、学号、姓名、Python成绩)
# 实现对学生信息及成绩的增、删、改、查方法
from student import Student
import os


class InfoMS:
    '''学生信息管理系统
    处理增、删、改、查功能逻辑
    '''
    def __init__(self, filename, encoding='utf-8'):
        self._encoding = encoding
        self._filename = filename
        # 用于保存学生信息
        self._infos = []
        self.__load()

    # 私有方法，用于将文件中的信息加载到内存中
    def __load(self):
        if not os.path.isfile(self.filename):
            return

        with open(self.filename, 'r', encoding=self._encoding) as f:
            for line in f:
                info = line.split()
                s = Student(info[0], info[1], info[2], int(info[3]))
                self._infos.append(s)

    @property
    def filename(self):
        # filename为只读属性，仅可在实例化是指定
        return self._filename

    @property
    def encoding(self):
        # encoding为只读属性
        return self._encoding

    def add(self, no, clz, name, score):
        '''增加学生信息，不可出现重复的学号'''
        i = self.findIndex(no)
        if i != -1:
            print('学号重复，添加失败')
        else:
            self._infos.append(Student(no, clz, name, score))

    def delete(self, no):
        '''删除指定学号的学生'''
        i = self.findIndex(no)
        if i == -1:
            print('指定学号的学生不存在 no: %s' % no)
        else:
            del self._infos[i]

    def update(self, no, clz, name, score):
        '''修改指定学号no的学生信息
        学号不可更改
        '''
        i = self.findIndex(no)
        if i == -1:
            print('指定学号的学生不存在 no: %s' % no)
        else:
            self._infos[i].clz = clz
            self._infos[i].name = name
            self._infos[i].score = score

    def find(self, no):
        '''返回指定学号的学生对象，找不到返回None'''
        i = self.findIndex(no)
        if i == -1:
            return None

        return self._infos[i]

    def findIndex(self, no):
        '''返回指定学号的学生在infos中的索引，找不到返回-1'''
        for i in range(len(self._infos)):
            if self._infos[i].no == no:
                break
        else:
            return -1

        return i

    def flush(self):
        '''将学生信息写入文件
        add()、delete()、update()方法做出的修改不会立刻写入文件，
        仅会将修改写入内存中，需要调用此方法将更改保存至文件
        '''
        with open(self.filename, 'w', encoding=self._encoding) as f:
            for s in self._infos:
                s.writeToFile(f)

    def printInfos(self):
        print('学号 班级 姓名 成绩')
        print('-' * 40)
        for s in self._infos:
            print('%-3s %s %s %3s' % (s.no, s.clz, s.name, s.score))


# 测试代码
if __name__ == '__main__':
    os.chdir('Homework/homework6/assign6')
    i = InfoMS('stu.txt')

    i.add('001', '1801', 'John', 60)
    i.add('003', '1802', 'Mary', 80)
    i.add('005', '1803', 'Peter', 99)
    i.printInfos()

    print()
    i.update('003', '1802', 'Mary', 90)
    i.delete('001')
    i.printInfos()

    # 保存更改
    i.flush()

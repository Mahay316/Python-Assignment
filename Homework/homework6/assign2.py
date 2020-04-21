# 2. 定义一个学生Student类，有下面的类属性：
#     姓名 name
#     年龄 age
#     成绩 score (语文, 数学, 英语) [每课成绩的类型为整数]
# 类方法：
#     获取学生的姓名：get_name() -> str
#     获取学生的年龄：get_age() -> int
#     返回3门科目中最高的分数：get_course() -> int
# 写好类以后，可以定义2个同学测试下


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        # score为元组，依次保存语文、数学和英语成绩
        self.score = score

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return max(self.score)


if __name__ ==  '__main__':
    s1 = Student('John', 18, (98, 80, 95))
    print(f'学生{s1.get_name()}，年龄{s1.get_age()}岁')
    print(f'最好成绩是{s1.get_course()}')

    s2 = Student('David', 20, (88, 79, 100))
    print(f'name: {s2.get_name()}')
    print('best score: %d' % s2.get_course())

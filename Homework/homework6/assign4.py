# 4. 封装一个学生类，有姓名、年龄、性别、语文成绩、数学成绩和英语成绩
# 封装方法，求单个学生的总分，平均分，以及打印学生的信息


class Student:
    GENDER_MALE = '男'
    GENDER_FEMALE = '女'

    def __init__(self, name, age, gender, score):
        self.name = name
        self.age = age
        self.gender = gender
        # score为元组，依次保存语文、数学和英语成绩
        self.score = score

    def __str__(self):
        info = f'姓名: {self.name} 性别: {self.gender} 年龄: {self.age}\n'
        score = f'语文: {self.score[0]} 数学: {self.score[1]} 英语: {self.score[2]}'
        return info + score

    def get_total(self):
        return sum(self.score)

    def get_average(self):
        return sum(self.score) / len(self.score)

    def info(self):
        print(self.__str__())


if __name__ == '__main__':
    s = Student('Peter', 18, Student.GENDER_MALE, (99, 89, 88))
    s.info()
    print('总分:', s.get_total(), '平均分:', s.get_average())

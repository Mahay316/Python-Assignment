# 2. 定义一个函数，判断一个输入的日期，是当年的第几周、周几
# 将程序改写一下，能针对我们学校的校历时间进行计算
# 校历第1周，2月17日 - 2月23日
# 校历第27周，8月17日 - 8月23日

from datetime import date

num_2_char = ['一', '二', '三', '四', '五', '六', '日']


# 以base为基准，计算target_date是第几周
# 并输出target_date是周几
def print_date(base, target_date):
    if target_date < base:
        print("日期格式有误，目标日期必须后于基准日期")
        return
    
    delta = target_date - base
    print("第{0}周, ".format(delta.days // 7 + 1), end="")
    print("星期{0}".format(num_2_char[target_date.weekday()]))


print("当前日期是今年的:")
print_date(date(2020, 1, 1), date.today())
print("当前日期是校历的:")
print_date(date(2020, 2, 17), date.today())

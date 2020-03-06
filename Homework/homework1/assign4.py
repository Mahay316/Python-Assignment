# 4. 判断用户输入的年份是否为闰年

year = int(input("请输入一个年份: "))
# 年份能被4整除而不能被100整除，或者能被400整除
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "是闰年")
else:
    print(year, "不是闰年")

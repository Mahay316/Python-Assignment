# 练习函数不定长参数的使用
def encap(*args):
    # 封装成列表
    print(list(args))
    # 封装成字典
    print({i: v for i, v in enumerate(args)})


encap(1, 3, 7, "Hi", True)

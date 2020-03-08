# 5. 写函数，检查传入字典的每一个value长度
# 如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者

from typing import Sized


def trim(m_dict):
    "将字典的所有value长度限制在2之内"
    for k, v in m_dict.items():
        # 判断是否可以计算长度
        if isinstance(v, Sized) and len(v) > 2:
            # 截取前两个内容
            m_dict[k] = v[0: 2]

    return m_dict


test_dict = {'a': [1, 3, 6, 7], 'b': 'abcadf', 'c': 123, 'd': (1, 2)}
print(trim(test_dict))

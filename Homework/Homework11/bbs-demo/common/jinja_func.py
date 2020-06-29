# functions invoked in Jinja templates
import re

type_map = ['编程语言', '学习交流', '影视文学',
            '电子竞技', '体育运动', '日常闲聊']


def type_to_str(msg_type):
    """convert message type represented by integer to string"""
    return type_map[msg_type]


def get_summary(html_content, length):
    """extract text from html to generate a short summary"""
    # remove HTML tags
    html_content = str(html_content)
    summary = re.sub('<.+?>', '', html_content)
    return summary[:length]

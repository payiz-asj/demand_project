# !/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
======================
@Project:截取文本文档中的中英文
@time:2019/10/18 0020:上午 4:18
@Author:ASJ
@email:Ai_shan_jiang@163.com
@File:
@Other:
======================
"""
import re
from typing import List


def cut_data(file: str):
    print("\t\ttxt从文件中读取目标语言字符\n")
    if file == '':
        file = input('输入文件名：')
    type: int = int(input('选择（1：中文  2：英文 3：数字）：'))
    line = []
    s: List[str] = []
    ss = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            s.append(line)
    res: str = ""
    if type == 1:
        for ii in s:
            res = "".join(re.findall('[\u4e00-\u9fa5]', ii)) + '\n'
            if res != '\n':
                ss.append(res)
    elif type == 2:
        for ii in s:
            res = "".join(re.findall('[\u0021-\u007a,\u0020]', ii)) + '\n'
            if res != '\n':
                ss.append(res)
    else:
        for ii in s:
            res = "".join(re.findall(r'\d+(?:\.\d+)?', ii)) + '\n'
            if res != '\n':
                ss.append(res)
    # re.findall(r'\b\d+\b', "hello,42 I'm a 32 str12312ing 30")  纯数字提取
    with open("分离结果.txt", 'w+', encoding='utf-8') as fp:
        for i in ss:
            fp.write(str(i))
    return ss
    pass


if __name__ == '__main__':
    cut_data('')
    print('\n分离完啦 ！\n')
    pass

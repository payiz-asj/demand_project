# !/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
======================
@Project:
@time:2019/10/20 0020:上午 7:24
@Author:ASJ
@email:Ai_shan_jiang@163.com
@File:
@Other:
======================
"""
import jieba  # 导入jieba中文分词包
import jieba.analyse
from os import path
from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt

# d = path.dirname(__file__)  # 该文件所在的文件夹路径
# font = os.path.join(os.path.dirname(__file__), "Roboto-Black.ttf")  # arialuni.ttf为字体的包


def ciyun(clod_text):
    path_img = "333.jpg"
    background_image = np.array(Image.open(
        path_img))  # keywords = jieba.analyse.extract_tags(sentence=str, topK=20, withWeight=True, allowPOS=('n', 'nr', 'ns'))
    # print(keywords)
    # Generate a word cloud image加载词云
    # image_colors = ImageColorGenerator(background_image)
    # 下面代码表示显示图片
    wor = WordCloud(
        # 设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
        font_path="C:/Windows/Fonts/simfang.ttf",
        # 设置了背景，宽高
        background_color="WHITE", width=2000, height=1000).generate(clod_text)
    # mask参数=图片背景，必须要写上，另外有mask参数再设定宽高是无效的

    # 生成颜色值
    # image_colors = ImageColorGenerator(background_image)
    # plt.imshow(wor.recolor(color_func=image_colors), interpolation="bilinear")
    fig, ax = plt.subplots()
    im = ax.imshow(wor, interpolation="bilinear")
    ax.axis("off")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.show()
    pass


def get_text():
    with open("英文需求.txt", "r") as fp:
        str = fp.read()
    str = str.lower()  # 数据清洗
    for ch in ["~!@#$%^&*()_+{}|[]\\||:;'<>?,./"]:
        str = str.replace(ch, " ")  # 分词
    return str
    pass


def count_english():
    eng = get_text()
    words = eng.split()  # 切片
    counts = {}  # 词频统计
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())  # 结果显示
    items.sort(key=lambda x: x[1], reverse=True)
    with open("top2.txt", 'w+', encoding='utf-8') as fp:
        # fp.write(''.join('单词：%s \t次数：%s\n' % x for x in items))
        fp.write(''.join('%s \n' % x[0] for x in items))
    clod_text = " ".join(words)
    # ciyun(clod_text)
    pass


def count_chi():
    with open("中文需求.txt", "r", encoding='utf-8') as fp:
        str = fp.read()
    words = jieba.lcut(str)  # 分词
    counts = {}  # 词频统计
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())  # 结果显示
    items.sort(key=lambda x: x[1], reverse=True)
    with open("top.txt", 'w+', encoding='utf-8') as fp:
        # fp.write(''.join('单词：%s \t次数：%s\n' % x for x in items))
        fp.write(''.join('%s \n' % x[0] for x in items))
    pass

if __name__ == '__main__':
    count_chi()
    count_english()

    print('\n我忙完了！\n')
    pass

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 5:58 下午
# @Author  : Albert Ma
# @File    : test1.py
from utils.db import DbCommit
from utils.db import DbQuery
import requests
from bs4 import BeautifulSoup

##################
# 唐诗300首代码开始
##################
numbers = []
dynasties = []
poets = []
names = []
poems = []


@DbCommit(db='lhrtest.db')
def insert(sql):
    return sql


for i in range(1, 20):
    i = str(i)
    url = 'http://www.shicimingju.com/shicimark/tangshisanbaishou_' + i + '_0__0.html'

    r = requests.get(url)
    demo = r.text  # 服务器返回响应

    soup = BeautifulSoup(demo, "html.parser")
    """
    demo 表示被解析的html格式的内容
    html.parser表示解析用的解析器
    """

    html1 = soup.find_all(class_='list_num_info')
    for text in html1:
        text = text.get_text().replace('\n', '').replace(' ', '').replace('[', '|').replace(']', '|')
        text = text.split('|')
        numbers.append(text[0])
        dynasties.append(text[1])
        poets.append(text[2])

    html2 = soup.find_all(class_='shici_list_main')
    for text in html2:
        text = text.get_text().replace('\n', '').replace(' ', '')
        text = text.replace('展开全文', '').replace('收起', '').replace('《', '').replace('》', '|')
        text = text.split('|')
        names.append(text[0])
        poems.append(text[1])

for value in zip(poets, dynasties, names, poems):
    poets, dynasties, names, poems = value
    sql = 'insert into poem(title,author,dynasty,poem) values (\'' + names + '\',\'' + poets + '\',\'' + dynasties + '\',\'' + poems + '\');'
    insert(sql)

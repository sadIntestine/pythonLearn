from utils.Log import Log
# -*- coding: utf-8 -*-
import chardet
from utils.db import DbCommit
from utils.db import DbQuery
import random


@DbCommit(db='lhrtest.db')
def insert(sql):
    return sql


@DbCommit(db='lhrtest.db')
def insert1111(sql, param=[]):
    print(sql)
    print(param)
    return sql, param


def resultInsert(result=[[]]):
    for i in result:
        sql = 'insert into weather(day,weather,highTemp,lowTemp) values (\'' + i[0] + '\',\'' + i[1] + '\',' + i[
            2] + ',' + i[3] + ');'
        print(sql)
        insert(sql)


# sql = '\'insert into weather(day,weather,highTemp,lowTemp) values (' + ','.join(i) + ')\''

@DbQuery(db='lhrtest.db')
def select(sql):
    return sql


if __name__ == '__main__':
    num = select('select count(0) from poem')
    id = random.randrange(0, num[0][0])
    s = select(str('SELECT * FROM poem ORDER BY RANDOM() limit 1'))
    print(s)
    poem = s[0][4].split('。')
    print(poem)
    index = random.randrange(0, len(poem)-1)
    consquence = poem[index].split('，')
    print(consquence)
    indexConsquence = random.randrange(0, len(consquence))
    print(consquence[indexConsquence])
    consquence.remove(consquence[indexConsquence])
    print(consquence)



from utils.Log import Log

from utils.db import DbCommit
from utils.db import DbQuery


@DbCommit(db='lhrtest.db')
def insert(sql):
    return sql


def resultInsert(result=[[]]):
    for i in result:
        sql = '\'insert into weather(day,weather,highTemp,lowTemp) values ('+','.join(i)+')\''
        print(sql)
        insert(sql)
  # sql = '\'insert into weather(day,weather,highTemp,lowTemp) values (?,?,?,?)\',(' + i[0] + ',' + i[1] + ',' + i[
  #           2] + ',' + i[3]+');'

@DbQuery(db='lhrtest.db')
def select(sql):
    return sql


# Press the green button in the gutter to run the script.
import bug
from utils.listTool import get_all_npy

if __name__ == '__main__':
    txt = bug.get_content('http://www.weather.com.cn/weather/101190101.shtml', )
    result = bug.get_data(txt)
    print(result)
   # resultInsert(result)
    insert('insert into weather(day,weather,highTemp,lowTemp) values (\'6日\', \'多云\', \'17\', \'5\')')
    # bug.write_data(result, 'weather.csv')
    # print(txt)10
    # print_hi('Py+Charm')
    # sqliteConnection
    # sqliteConnection.test("夏凡")
    # lg.run_game()
    # select('select * from user')

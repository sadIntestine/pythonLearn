import requests
import re
import csv
from utils.db import DbCommit
import time

from utils.db import DbQuery
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    # 'referer': 'https://dytt8.net/html/gndy/dyzz/list_23_2.html'
}
BASE_DOMIN = 'https://www.gushiwen.cn/default_1.aspx'
def parse_page(url):
    response = requests.get(url, headers=headers)
    text = response.text
    titles = re.findall(r'<b>(.*?)</b>', text, flags=re.DOTALL)  #  flags=re.DOTALL 来对这些 tab, new line 不敏感.
    authors=re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>', text, flags=re.DOTALL)
    dynasty=re.findall(r'<p class="source">.*?<a.*?<a.*?>(.*?)</a>', text, flags=re.DOTALL)
    poems_ret= re.findall(r'<div class="contson".*?>(.*?)</div>', text, flags=re.DOTALL)
    poems=[]
    for poem in poems_ret:
        temp = re.sub("<.*?>", "", poem)
        poems.append(temp.strip())
    results = []
    result = []
    for value in zip(titles, dynasty, authors, poems):
        title, time, author, poem = value
        sql = 'insert into poem(title,author,dynasty,poem) values (\'' + title + '\',\'' + time + '\',\'' + author + '\',\'' + poem + '\');'
        insert(sql)
        result.append(title)
        result.append(time)
        result.append(author)
        result.append(poem)
    results.append(result)
    return results
def spider():
    #url_base = 'https://so.gushiwen.cn/shiwens/default.aspx?page={}&tstr=&astr=%E6%9D%8E%E7%99%BD'
    url_base = 'https://www.gushiwen.cn/default_{}.aspx'
    for i in range(1, 100):
        print('正在爬取第{}页：'.format(i))
        url = url_base.format(i)
        time.sleep(1)
        results = parse_page(url)
        # write_data(results,'poem.csv')

@DbCommit(db='lhrtest.db')
def insert(sql):
    return sql

def write_data(data, name):
    file_name = name
    with open(file_name, 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)

if __name__ == '__main__':
    spider()
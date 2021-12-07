# -*- coding: utf-8 -*-
import requests
import csv
import random
import time
import socket
import http.client
from lxml import etree
# import urllib.request
from bs4 import BeautifulSoup


def get_content(url, data=None):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    timeout = random.choice(range(80, 180))
    while True:
        try:
            rep = requests.get(url, headers=header, timeout=timeout)
            rep.encoding = 'utf-8'
            # req = urllib.request.Request(url, data, header)
            # response = urllib.request.urlopen(req, timeout=timeout)
            # html1 = response.read().decode('UTF-8', errors='ignore')
            # response.close()
            break
        # except urllib.request.HTTPError as e:
        #         print( '1:', e)
        #         time.sleep(random.choice(range(5, 10)))
        #
        # except urllib.request.URLError as e:
        #     print( '2:', e)
        #     time.sleep(random.choice(range(5, 10)))
        except socket.timeout as e:
            print('3:', e)
            time.sleep(random.choice(range(8, 15)))

        except socket.error as e:
            print('4:', e)
            time.sleep(random.choice(range(20, 60)))

        except http.client.BadStatusLine as e:
            print('5:', e)
            time.sleep(random.choice(range(30, 80)))

        except http.client.IncompleteRead as e:
            print('6:', e)
            time.sleep(random.choice(range(5, 15)))

    return rep.text
    # return html_text


def get_data(html_text):
    numbers = []
    dynasties = []
    poets = []
    names = []
    poems = []
    bs = BeautifulSoup(html_text, "html.parser")  # 创建BeautifulSoup对象
    html1 = bs.find(class_ = 'card shici_card')
    for i in html1:
        print(i.find(class_ = 'shici_content'))
    # for text in html1:
    #     text1 = text.find(class_ = 'list_num_info').get_text().replace('\n', '').replace(' ', '').replace('[', '|').replace(']', '|')
    #     text1 = text1.split('|')
    #     text2 = text.get_text().replace('\n', '').replace(' ', '')
    #     text2 = text2.replace('展开全文', '').replace('收起', '').replace('《', '').replace('》', '|')
    #     text2 = text2.split('|')



def write_data(data, name):
    file_name = name
    with open(file_name, 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)


if __name__ == '__main__':
    for i in range(1, 2):
        i = str(i)
        url = 'http://www.shicimingju.com/shicimark/tangshisanbaishou_' + i + '_0__0.html'
        result = get_content(url)
        get_data(result);
        # print(result.encode("gbk", "ignore"))

from datetime import date
from lxml import etree
import requests
import sys
import random
import time
import socket
import http.client


class shigeSpider():

    def download(self, url):
        self.domain = url.split('/')[2]
        data = self.get_content(url)
        if data:
            self.parse(data)

    def parse(self, data):
        response = etree.HTML(data)
        for row in response.xpath('//div[@class="left"]/div[@class="sons"]'):
            title = row.xpath('div[@class="cont"]/p/a/b/text()')[0] if row.xpath('div[@class="cont"]/p/a/b/text()') else ''
            dynasty = row.xpath('div[@class="cont"]/p[@class="source"]//text()')[0] if row.xpath('div[@class="cont"]/p[@class="source"]//text()') else ''
            author = row.xpath('div[@class="cont"]/p[@class="source"]//text()')[-1] if row.xpath('div[@class="cont"]/p[@class="source"]//text()') else ''
            content = ''.join(row.xpath('div[@class="cont"]/div[@class="contson"]//text()')).replace('　　', '').replace('\n', '') if row.xpath('div[@class="cont"]/div[@class="contson"]//text()') else ''
            tag = ','.join(row.xpath('div[@class="tag"]/a/text()')) if row.xpath('div[@class="tag"]/a/text()') else ''
            self.db.add_new_row('shigeSpider', { 'title': title, 'dynasty': dynasty, 'author': author, 'content': content, 'tag': tag, 'createTime': str(date.today()) })
            print ('Title: {}'.format(title))
        if response.xpath('//div[@class="pages"]/a/@href'):
            self.download('http://' + self.domain + response.xpath('//div[@class="pages"]/a/@href')[-1])

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

if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    url = 'http://so.gushiwen.org/type.aspx'
    do = shigeSpider()
    do.download(url)
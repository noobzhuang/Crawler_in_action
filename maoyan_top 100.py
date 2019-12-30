import requests
import re
import json
from requests.exceptions import RequestException
import time


def get_one_page_html(url,header):
    try:
        r=requests.get(url,headers=header)
        if r.status_code==200:
            return r.text
    except RequestException:
        return  None


def get_html_items(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?<p.*?name.*?boarditem-click.*?>(.*?)</a></p>' +
                         '.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>' +
                         '.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>', re.S)
    # pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?<a.*?data-act.*?data-val.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>'+
    #                      '.*?integer.*?>(.*?)</li>', re.S)
    items=re.findall(pattern,html)
    for item in items:
        yield {
            '排名': item[0],
            '片名 ': item[1],
            '主演': item[2].strip()[3:],
            '上映时间': item[3].strip()[5:],
            '评分': item[4] + item[5]  # 将评分信息连接起来
        }
def write_out(content):
    with open('E:/Desktop/10.18.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()

def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    header = {'Origin': 'https://maoyan.com',
              'Referer': 'https://maoyan.com/films/1203',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}
    html=get_one_page_html(url,header)
    for item in get_html_items(html):
        print(item)
        write_out(item)

if __name__ == '__main__':
    for i in range(10):
        main(i*10)
# main(i * 10)  # 构造参数offset，达到翻页的效果。>(\d+)</i>.*?data-val=.*?>(\w+)</a></p>.*?class="star">(\w+?)</p>



import re
import requests
import json

def get_item(url):
    r=requests.get(url)
    pa=re.compile('<div class="title".*?data-sl.*?>(.*?)</a>.*?'+
                  '<a.*?region.*?>(.*?)</a>.*?'+
                  '<span.*?houseIcon.*?</span>(.*?)</div>.*?'+
                  '<span.*?starIcon.*?n>(.*?)</div>',re.S)
    v=re.findall(pa,r.text)
    for item in v:
        yield {
            '标题':item[0],
            '地址':item[1],
            '描述':item[2],
            '关注人数':item[-1]
                }
def write_out_txt(content):
    with open('E:/Desktop/Lianjia.txt', 'a+', encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def write_out_csv(content):




def main(offset):
    url = 'https://gz.lianjia.com/ershoufang/pg'+str(offset)
    items=get_item(url)

    for item in items:
        print(item)
        write_out_txt(item)


if __name__=='__main__':
    for i in range(1,3):
        main(i)
import requests, os
from bs4 import BeautifulSoup
from wget import download
from urllib.request import urlretrieve

proxies = {
  "http": "http://127.0.0.1:7890",
  "https": "http://127.0.0.1:7890",
}

os.chdir("D:\H\本子\kenkano saisen")
url_head = "https://nhentai.net/g/335675/"
page_num = 1
while 1:
    try:
        url = url_head + str(page_num)
        data = requests.get(url, proxies=proxies).text
        status_code = requests.get(url, proxies=proxies).status_code
        if status_code > 200:
            print("爬取完成，告辞")
            break
        soup = BeautifulSoup(data, 'html.parser')
        pic_label = soup.find_all('img', width="960")
        for i in pic_label:
            pic_link = i['src']
        pic_name = str(page_num) + ".jpg"
        #download(pic_link, out=pic_name)
        urlretrieve(pic_link, pic_name)
        print("已爬取：", pic_link)
        page_num = page_num + 1
    except:
        print("出现迷之问题")
        page_num = page_num + 1
        continue
import requests, os
from bs4 import BeautifulSoup


proxies = {
  "http": "http://127.0.0.1:7890",
  "https": "http://127.0.0.1:7890",
}



page_num = input("请输入页数：")
url_head = "https://nhentai.net/g/"
url = url_head + str(page_num) + '/1'
data = requests.get(url, proxies=proxies).text
soup = BeautifulSoup(data, 'html.parser')
pic_label = soup.find_all('img', width="1280")
for i in pic_label:
    pic_link = i['src']

print(pic_link)
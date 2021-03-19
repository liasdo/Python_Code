import requests,lxml
import os
from bs4 import BeautifulSoup

page_num = input("请输入页数：")
url_head = "https://nhentai.net/g/"
url = url_head + str(page_num) + '/1'
data = requests.get(url).text
#soup = BeautifulSoup(data, 'html.parser')
#pic_label = soup.find_all('img', width="1280")

print(data)
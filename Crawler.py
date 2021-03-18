import requests,lxml
from bs4 import BeautifulSoup

url_head = "https://baidu.com/"
page_num = input("请输入页数：")
url = url_head + str(page_num)
print(url)
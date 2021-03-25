import requests
from bs4 import BeautifulSoup
import os
# 请求地址
url = 'http://www.xiaohuar.com/list-1-1.html'
html = requests.get(url).content
# BeautifulSoup 实例化
soup  = BeautifulSoup(html,'html.parser')
jpg_data = soup.find_all('img',width="210")
for i in jpg_data:
    data = i['src']
    name = i['alt']
# 判断URL是否完整
    if "https://www.dxsabc.com/" not in data:
        data = 'http://www.xiaohuar.com'+ data
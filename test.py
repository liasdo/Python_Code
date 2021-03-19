import requests
import os
from bs4 import BeautifulSoup

url = "https://www.baidu.com"
res = requests.get(url)
data = res.text
print(data)
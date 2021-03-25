import requests, os
from bs4 import BeautifulSoup
from wget import download
from urllib.request import urlretrieve

os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"



os.chdir("D:\H\本子\Test")
dir = '/g/335675/'
url_head = "https://nhentai.net/" + dir
page_num = 1

url = url_head + str(page_num)
data = requests.get(url).text
status_code = requests.get(url).status_code

soup = BeautifulSoup(data, 'html.parser')
pic_label = soup.find_all('img', width="960")

print(pic_label)

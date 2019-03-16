# coding : utf-8
import requests
from bs4 import BeautifulSoup

r = requests.get("http://news.163.com/")
soup = BeautifulSoup(r.content,'html.parser',from_encoding="gb18030")
for i in soup.find_all('a'):
    try:
        print(i["href"])
    except Exception as e:
        pass
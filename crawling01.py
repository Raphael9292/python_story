# get HTML Page, Parsing HTML/CSS, export data
import os.path
import requests
from bs4 import BeautifulSoup

URL = ('https://finance.naver.com/news/mainnews.nhn')
# RESULT_DIR = os.path.dirname('C:\\Users\\Administrator\\Desktop\\python_story\\result')

# HTTP GET Request
req = requests.get(URL)

# HTML source
html = req.text

# How to Parse
soup = BeautifulSoup(html, 'html.parser')

# take selector
news_titles = soup.select('dd.articleSubject')

# print data
print(news_titles)

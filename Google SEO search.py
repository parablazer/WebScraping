import html
import SelSearch
import requests.models
from bs4 import BeautifulSoup
import requests_html
from requests_html import HTMLSession
from requests_html import HTML


session=HTMLSession()

sengine = ['https://duckduckgo.com/?q=', 'https://www.google.com/search?q=', 'https://www.bing.com/search?q=']
keyword = 'cnn'

def SearchResultMini():

   for results in sengine:
     soup = []
     html_text = requests.get(results + keyword).text
     soup = BeautifulSoup(html_text, 'lxml')
     data = [soup]
     print(data)

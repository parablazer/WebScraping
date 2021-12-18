
import html
import selenium
import requests.models
from bs4 import BeautifulSoup
import requests_html
from requests_html import HTMLSession
from requests_html import HTML


site = 'https://github.com/parablazer'
response = session.get(site).text

with open(response) as htmlfile:
  sourcecode = htmlfile.read()
  parsedHtml = HTML(html=sourcecode)
  parsedHtml.render()

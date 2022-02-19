from requests_html import HTMLSession, HTML
from bs4 import BeautifulSoup
from lxml.html import fromstring
import os
import requests

html = HTML

dir = '/home/dominik/cifs/mycloud/Survival/'


s = HTMLSession()
url = 'http://www.survivorlibrary.com/library-download.html'

r = s.get(url)


r.html.render(sleep=1)

links = r.html.xpath('/html/body/div/div/div/main/div[2]/div[3]/center/table/tbody', first=True)
list = links.absolute_links
#print(list)

for i in list:

    # get title tag
    p = s.get(i)
    page = fromstring(p.content)
    title = page.findtext('.//title')
    # print(title)
    # Make directory with title name
    dir_location = dir + title
    if not os.path.exists(dir_location):
        os.makedirs(dir_location)
    # get pdf links
    plink = p.html.xpath('/html/body/div/div/div/main/div[2]/div[2]/table/tbody', first=True)
    plist = plink.absolute_links
    print(plist)
    for pdf in plist:
        g = s.get(pdf, stream=True)
        if ('.pdf' in pdf):
            print('Downloading File ' + pdf)

            with open('/home/dominik/cifs/mycloud/Survival/' + title + '/' + pdf[39:], 'wb') as f:
                f.write(g.content)
                f.close()
        print(pdf + 'Downloaded')

print('All Files Downloaded')















#articles = r.html.find('article')
#title = article.find('h3', first=True).text
#print(title)



#for article in articles:
 #   title = article.find('h3', first=True).text
#    desc = article.find('p', first=True).text
#    link = article.find('a', first=True)
#
#    print(title)
#    print(desc)
#    print(link.attrs['href'])
#    print()
#
#    csv_writer.writerow([title, desc, link])
#csv_file.close()



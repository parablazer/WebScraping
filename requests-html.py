from requests_html import HTMLSession, HTML
import csv
html = HTML
#csv_file = open('page_scrape.csv', 'w')
#csv_writer = csv.writer(csv_file)
#csv_writer.writerow(['title', 'desc', 'link'])

s = HTMLSession()
url = 'https://duckduckgo.com/?q=cnn&t=h_&ia=web'

r = s.get(url)

r.html.render(sleep=1)

links = r.html.xpath('//*[@id="links"]', first=True)
print(links)















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



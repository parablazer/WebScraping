from requests_html import HTMLSession, HTML
import csv

csv_file = open('page_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'desc', 'link'])
session = HTMLSession()
r = session.get('https://parablazer.github.io/')

articles = r.html.find('article')
#title = article.find('h3', first=True).text
#print(title)




for article in articles:
    title = article.find('h3', first=True).text
    desc = article.find('p', first=True).text
    link = article.find('a', first=True)

    print(title)
    print(desc)
    print(link.attrs['href'])
    print()

    csv_writer.writerow([title, desc, link])
csv_file.close()



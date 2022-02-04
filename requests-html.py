from requests_html import HTMLSession, HTML

html = HTML


s = HTMLSession()
url = 'https://duckduckgo.com/?q=microsoft&t=h_&ia=web'

r = s.get(url)

r.html.render(sleep=1)

links = r.html.xpath('//*[@id="links"]', first=True)
print(links)

print(links.absolute_links)













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



from bs4 import BeautifulSoup
import requests



with open('scrape.html') as scraped:
    soup = BeautifulSoup(scraped,'html.parser')

#print(soup.prettify())

"""
# the term article used here is a varible
article = soup.find('div', class_='article')
#print(match)

headline = article.h2.a.text
print(headline)

summary = article.p.text
print(summary)
  """

# the term article used here is a varible
for article in soup.find_all('div', class_='article'):
    #print(match)

    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)
    print()


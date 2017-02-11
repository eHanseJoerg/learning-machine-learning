import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        #url = 'https://buckysroom.org/trade/search.php' + str(page)
        url = 'http://www.imdb.com/movies-in-theaters/'
        source_code = requests.get(url)
        plain_text = source_code.text  #get rid of extra crap in the html element
        #Jetzt müssen wir das ganze in ein BeatifulSoup Objekt umwandeln:
        soup = BeautifulSoup(plain_text, 'lxml')
        #Das Soup Objekt ist das Objekt, durch das wir sortieren etc. können
        for link in soup.findAll('a'):
            #Hier loopen wir durch alle Tags des HTML Docukments und finden alle
            #Links im Dokument. Wir filtern nur die Links raus, die die Klasse "item-name" haben.
            href = link.get('href')
            linkstring = link.text
            print(href)
            print('Linkstring: ' + linkstring)
        page += 1


trade_spider(1)

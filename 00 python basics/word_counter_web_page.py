import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'lxml')
    for link in soup.findAll('a'):
        content = link.text
        words = content.lower().split()
        for word in words:
            word_list.append(word)
    cw = clean_up_list(word_list)
    for w in cw:
        print(w)


def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        #symbols = list('!\"§$%&/()=?\'´¹²³¼½¬{[]}\\+*#-.,;:_<>|©')
        cleanword = ''.join(e for e in word if e.isalnum())
        if len(cleanword) > 0:
            clean_word_list.append(cleanword)
    return clean_word_list


start(url = 'http://www.imdb.com/movies-in-theaters/')

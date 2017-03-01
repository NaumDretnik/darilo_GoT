from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

print("Darilo\n")

url = "http://quotes.yourdictionary.com/theme/marriage/"
html = urlopen(url).read()

prva_stran = BeautifulSoup(html)

"""quotes = []

for quote in prva_stran.findAll("p", {"class": "quoteContent"}):
    quotes.append(quote.text)

for citat in quotes[:5]:
    print(citat + "\n____________________________________________________\n")"""

for quote in prva_stran.findAll("p", {"class": "quoteContent"}, limit=5):
    print(quote.text + "\n____________________________________________________________\n")



"""for quote in prva_stran.findAll("p", {"class": "quoteContent"}):
    quotes = []
    quotes.append(quote.text)
    for citat in quotes[:5]:
        print(citat)

Zakaj v tem primeru slicing ne deluje?"""





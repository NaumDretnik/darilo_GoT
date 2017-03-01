from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
import re



url = "https://en.wikipedia.org/wiki/Game_of_Thrones"
html = urlopen(url).read()

osnovna_stran = BeautifulSoup(html)

sezone = []

skupno_stevilo = []

for season in osnovna_stran.findAll("a", {"href": re.compile("/wiki/Game_of_Thrones_\(season")}):
    if season["href"] not in sezone:
        sezone.append(season["href"])

for href in sezone:
    url_sezone = ("https://en.wikipedia.org" + href)
    html_sezone = urlopen(url_sezone).read()
    sezona_BS = BeautifulSoup(html_sezone)

    tabela = sezona_BS.find("table", {"class":"wikitable plainrowheaders wikiepisodetable"})

    if tabela:
        vrstica = tabela.findAll("tr", {"class": "vevent"})

        if vrstica:
            for stevilo in vrstica:
                stevilo_gledalcev = stevilo.findAll("td")[5]
                stevilo.sup.decompose()
                mnozica = stevilo_gledalcev.text
                skupno_stevilo.append(float(mnozica))


print("A total of %s million people watched the airings of GoT episodes." %sum(skupno_stevilo))
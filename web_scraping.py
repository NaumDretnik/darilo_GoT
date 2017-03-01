from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

csv_file = open("email_list.csv", "w")

url = "https://scrapebook22.appspot.com/"
html = urlopen(url).read()

prva_stran = BeautifulSoup(html)

# print(prva_stran.html.head.title.string)  .string za vrednost znotraj tagov

csv_file.write("Name, Email, City\n")

for povezava in prva_stran.findAll("a"):
    if povezava.string == "See full profile":
        url_profila = (url + povezava["href"])
        html_profila = urlopen(url_profila).read()

        profil = BeautifulSoup(html_profila)
        url_profila = (url + povezava["href"])
        html_profila = urlopen(url_profila).read()

        div = profil.find("div", {"class": "col-md-8"})
        ime = div.find("h1")
        print(ime.string)


        email_span = profil.find("span", {"class": "email"})
        print(email_span.string)

        vsi_spani = profil.findAll("span")
        for s in vsi_spani:
            if s.has_key("data-city"):
                print(s.string)
                break

        print("_______________________________")
        print(" ")

        csv_file.write(str(ime.string) + ", " + str(email_span.string) + ", " + str(s.string) + "\n")

csv_file.close()
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import ssl


def get_auction(url):
    newclient = uReq(url, context=context)
    new_html = newclient.read()
    newclient.close()

    new_soup = soup(new_html, "html.parser")


aucLocation_url = 'https://www.iaai.com/locations'
context = ssl._create_unverified_context()
uClient = uReq(aucLocation_url, context=context)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
locations = page_soup.findAll("a", {"class":"detailsLink"})

locations_file = open('iaai_locations.txt', 'w+')
for i in range(0, len(locations)):
    locations_file.write(str(locations[i]) + "\n")
    html = str(locations[i])
    location_url = 'https://iaai.com'
    x = 29
    doubleQ = '"'
    while html[x] != doubleQ:
        location_url += html[x]
        x += 1

    get_auction(location_url)





    new_soup = soup(new_html, "html.parser")


aucLocation_url = 'https://www.iaai.com/locations'
context = ssl._create_unverified_context()
uClient = uReq(aucLocation_url, context=context)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
locations = page_soup.findAll("a", {"class":"detailsLink"})

locations_file = open('iaai_locations.txt', 'w+')
for i in range(0, len(locations)):
    locations_file.write(str(locations[i]) + "\n")
    html = str(locations[i])
    location_url = 'https://iaai.com'
    x = 29
    doubleQ = '"'
    while html[x] != doubleQ:
        location_url += html[x]
        x += 1

    get_auction(location_url)




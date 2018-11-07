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
print("Loading...")
page_html = uClient.read()
print("Loading...")
uClient.close()

page_soup = soup(page_html, "html.parser")
print("Loading...")
locations = page_soup.findAll("a", {"class":"detailsLink"})
print("Loading...")
locations_file = open('iaai_locations.txt', 'w+')
for i in range(0, len(locations)):
    locations_file.write(str(locations[i]) + "\n")
    print("Loading for loop... " + str(i) + " out of " + str(len(locations)))
    html = str(locations[i])
    location_url = 'https://iaai.com'
    x = 29
    doubleQ = '"'
    while html[x] != doubleQ:
        location_url += html[x]
        print("Loading while..." + str(x) + " out of " + str(len(locations)))
        x += 1
    print(location_url)
    print("Get Auction for " + str(i))
    get_auction(location_url)

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import ssl
context = ssl._create_unverified_context()


def get_cars(url):
    file = open("get_car.txt", "w+")
    newclient = uReq(url, context= context)
    new_html = newclient.read()
    print(new_html)
    newclient.close()

    new_soup = soup(new_html, "html.parser")
    car_year_soup = new_soup.findAll("td", {"class" : "info year"})
    print("There are " + str(len(car_year_soup)) + " cars in this auction")


def get_auction(url):
    newclient = uReq(url, context=context)
    new_html = str(newclient.read())
    newclient.close()

    new_soup = soup(new_html, "html.parser")
    auction_this_day = new_soup.findAll("a", {"class":"details-auc-date"})
    print("There are " + str(len(auction_this_day)) + " auctions in this location")
    print(auction_this_day[0])
    html = str(auction_this_day)
    print(html[34])
    locations_file = open('iaai_location.txt', 'w+')
    for i in range(0, len(auction_this_day)):
        locations_file.write(str(auction_this_day[i]) + "\n")
        print("Loading for loop... " + str(i) + " out of " + str(len(auction_this_day)))
        html = str(auction_this_day[i])
        location_url = 'https://iaai.com'
        x = 34
        doubleQ = '"'
        while html[x] != doubleQ:
            location_url += html[x]
            print("Loading while..." + str(x) + " out of " + str(len(auction_this_day)))
            x += 1
        print(location_url)
        print("Get Auction for " + str(i))

        get_cars(url)


def initiate():
    aucLocation_url = 'https://www.iaai.com/locations'
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


# initiate()
# get_auction("https://www.iaai.com/locations/140/albuquerque")
# get_cars("https://iaai.com/Auctions/BranchListingView.aspx?branchCode=626&amp;aucDate=12122018")

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import ssl
from CarClass import Car
context = ssl._create_unverified_context()


def get_cars(url):
    car_list = []
    file = open("get_car.txt", "w+")
    newclient = uReq(url, context= context)
    new_html = newclient.read()
    print(new_html)
    newclient.close()
    new_soup = soup(new_html, "html.parser")

    # Scrape the year
    car_year_soup = new_soup.findAll("td", {"class": "info year"})
    indexes = []
    for i in range(0, len(car_year_soup)):
        year = ""
        strng = str(car_year_soup[i])
        for x in range(24, 29):
            year += str(strng[x])

        if int(year) >= 2016:
            indexes.append(i)
            car_list.append(Car(int(year)))

    # Scrape the make
    car_make_soup = new_soup.findAll("td", {"class": "info make"})
    c = 0
    while c < len(indexes):
        make = ""
        strng = str(car_make_soup[indexes[c]])
        x = 24
        while strng[x] != "<":
            make += strng[x]
            x += 1
        car_list[c].make = make
        c += 1

    # Scrape the model
    car_model_soup = new_soup.findAll("td", {"class": "info model"})
    c = 0
    while c < len(indexes):
        model = ""
        strng = str(car_model_soup[indexes[c]])
        x = 24
        while strng[x] != "<":
            model += strng[x]
            x += 1
        car_list[c].model = model
        c += 1

    for i in range(0, len(car_list)):
        print(str(car_list[i].year) + " " + car_list[i].make + " " + car_list[i].model)


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
    # Open a connection between the program and IAAI website
    uClient = uReq(aucLocation_url, context=context)
    print("Loading...")
    # Copies the html code into the variable page_html
    page_html = uClient.read()
    print("Loading...")
    uClient.close()

    page_soup = soup(page_html, "html.parser")
    print("Loading...")
    locations = page_soup.findAll("a", {"class": "detailsLink"})
    print("Loading...")
    locations_file = open('iaai_locations.txt', 'w+')

    # Scrapes the link
    for i in range(0, len(locations)):
        locations_file.write(str(locations[i]) + "\n")
        print("Working on Location " + str(i) + " out of " + str(len(locations)))
        html = str(locations[i])
        location_url = 'https://iaai.com'
        x = 29
        doubleQ = '"'
        while html[x] != doubleQ:
            location_url += html[x]
            x += 1
        print(location_url)
        print("Get Auction for " + str(i))
        get_auction(location_url)


# initiate()
# get_auction("https://www.iaai.com/locations/140/albuquerque")
get_cars("https://www.iaai.com/Auctions/BranchListingView.aspx?branchCode=711&aucDate=12282018")

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import ssl
from CarClass import Car
import datetime
context = ssl._create_unverified_context()

car_list = []


def get_cars(url):
    newclient = uReq(url, context= context)
    new_html = newclient.read()
    print(new_html)
    newclient.close()
    new_soup = soup(new_html, "html.parser")

    # Scrape the year
    car_year_soup = new_soup.findAll("td", {"class": "info year"})
    indexes = []
    previous_list = len(car_list)
    for i in range(0, len(car_year_soup)):
        year = ""
        strng = str(car_year_soup[i])
        for x in range(24, 29):
            year += str(strng[x])
        print(strng + " || " + year)
        if int(year) >= 2016:
            indexes.append(i)
            car_list.append(Car(year))

    print("There are " + str(len(indexes)) + " qualifying vehicles in this auction")

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
        print(strng + " || " + make)
        car_list[c + previous_list].make = make
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
        print(strng + " || " + model)
        car_list[c + previous_list].model = model
        c += 1

    # Scrape the damage


def get_auction(url):
    newclient = uReq(url, context=context)
    new_html = str(newclient.read())
    newclient.close()

    new_soup = soup(new_html, "html.parser")
    auction_this_day = new_soup.findAll("a", {"class":"details-auc-date"})
    print("There are " + str(len(auction_this_day)) + " auctions in this location")
    html = str(auction_this_day)
    date = ""
    for x in range(95, 103):
        date += html[x]
    print(date)
    if check_date(date):
        locations_file = open('iaai_location.txt', 'w+')
        for i in range(0, len(auction_this_day)):
            locations_file.write(str(auction_this_day[i]) + "\n")
            html = str(auction_this_day[i])
            location_url = 'https://iaai.com'
            x = 34
            doubleq = '"'
            while html[x] != doubleq:
                location_url += html[x]
                x += 1
            print(location_url)
            print("Get Auction for " + str(i))

            get_cars(url)
    else:
        print("This auction was omitted")


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
        print("Working on Location #" + str(i) + " out of " + str(len(locations)))
        html = str(locations[i])
        location_url = 'https://iaai.com'
        x = 29
        doubleq = '"'
        while html[x] != doubleq:
            location_url += html[x]
            x += 1
        print(location_url)
        get_auction(location_url)


def check_date(date):

    on_bound = True
    now = datetime.datetime.now()
    month = date[0] + date[1]
    day = date[2] + date[3]
    year = date[4] + date[5] + date[6] + date[7]

    week = now.date().isocalendar()[1] + 2

    d = str(now.year) + "-W" + str(week)
    r = datetime.datetime.strptime(d + '-0', "%Y-W%W-%w")
    print(r.month)
    print(month)

    if r.month >= int(month) and on_bound:
        print("yes")

    if r.year == int(year):
        print(str(r.year) + " | " + year)
        on_bound = True
        if r.month >= int(month) and on_bound:
            print(str(r.month) + " | " + month)
            on_bound = True
            if 1 <= int(day) <= r.day and on_bound:
                print(str(r.day) + " | " + day)
                on_bound = True
            else:
                on_bound = False
        else:
            on_bound = False
    else:
        on_bound = False

    print("Auction in is in bound")
    return on_bound


initiate()
# get_auction("https://www.iaai.com/locations/140/albuquerque")
# get_cars("https://www.iaai.com/Auctions/BranchListingView.aspx?branchCode=711&aucDate=12282018")

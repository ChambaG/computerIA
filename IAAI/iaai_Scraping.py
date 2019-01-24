from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import ssl
from CarClass import Car
import datetime
context = ssl._create_unverified_context()


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


def get_auction(url):
    newclient = uReq(url, context=context)
    new_html = str(newclient.read())
    newclient.close()

    new_soup = soup(new_html, "html.parser")
    auction_this_day = new_soup.findAll("a", {"class":"details-auc-date"})
    print("There are " + str(len(auction_this_day)) + " auctions in this location")
    html = str(auction_this_day)
    locations_file = open('iaai_location.txt', 'w+')
    for i in range(0, len(auction_this_day)):
        date = ""
        locations_file.write(str(auction_this_day[i]) + "\n")
        html = str(auction_this_day[i])
        location_url = 'https://iaai.com'
        x = 34
        doubleq = '"'
        while html[x] != doubleq:
            location_url += html[x]
            x += 1
        for y in range(76, 84):
            date += location_url[y]
        print(location_url)
        if check_date(date):
            print(date)
            print("Get Cars from auction #" + str(i + 1) + " out of " + str(len(auction_this_day)))
            get_cars(location_url)


def get_cars(url):
    newclient = uReq(url, context= context)
    new_html = newclient.read()
    newclient.close()
    new_soup = soup(new_html, "html.parser")

    car_year_soup = new_soup.findAll("td", {"class": "info year"})
    indexes = []
    for i in range(0, len(car_year_soup)):
        year = ""
        strng = str(car_year_soup[i])
        for x in range(24, 29):
            year += str(strng[x])
        if int(year) >= 2016:
            indexes.append(i)

    print("There are " + str(len(indexes)) + " qualifying vehicles in this auction")
    car_list = [Car() for x in range(len(indexes))]

    # Scrape the year
    i = 0
    while i < len(indexes):
        year = ""
        strng = str(car_year_soup[indexes[i]])
        for x in range(24, 29):
            year += str(strng[x])
        car_list[i].year = int(year)
        i += 1

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
        make = "".join(make.splitlines())
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
        model = "".join(model.splitlines())
        car_list[c].model = model
        c += 1

    # Get the link of the vehicle to scrape additional information
    car_link = new_soup.findAll("td", {"class": "info secondCol stockNbr"})
    for i in range(0, len(indexes)):
        car_url = "https://www.iaai.com"
        code = str(car_link[indexes[i]])
        for x in range(92, 133):
            car_url += code[x]
        if car_url.find("/Vehicle?") == -1:
            car_url = "https://www.iaai.com"
            for y in range(179, 220):
                car_url += code[y]
        car_list[i].url = cleanup(car_url)

    # Scrape the Bid and Damage
    for i in range(0, len(indexes)):
        newer_client = uReq(car_list[i].url, context=context)
        newer_html = newer_client.read()
        newer_client.close()
        souping = soup(newer_html, "html.parser")

        # Scraping the bid
        bid_soup = souping.findAll("span", {"class": "high-price"})
        bid_soup_str = str(bid_soup)
        bid = ""
        c = 27
        while c < len(bid_soup_str) and bid_soup_str[c] != "<":
            bid += bid_soup_str[c]
            c += 1
        bid = bid.replace(',', '')
        car_list[i].bid = bid

        # Scraping the damage
        damage_soup = souping.findAll("div", {"class": "col-7 col-value flex-self-end"})
        damage_soup_str = str(damage_soup[1])
        damage = ""
        c = 54
        while c < len(damage_soup_str) and damage_soup_str[c] != "<":
            if damage_soup_str[c] == " " and damage_soup_str[c + 1] == "<":
                c = len(damage_soup_str)
            else:
                damage += damage_soup_str[c]
                c += 1
        damage = damage.replace("&amp;", "&")
        car_list[i].damage = damage
    print()
    for i in range(0, len(indexes)):
        car_list[i].show()



def check_date(date):

    on_bound = True
    now = datetime.datetime.now()
    month = date[0] + date[1]
    day = date[2] + date[3]
    year = date[4] + date[5] + date[6] + date[7]

    week = now.date().isocalendar()[1] + 1

    d = str(now.year) + "-W" + str(week)
    # Limit date
    r = datetime.datetime.strptime(d + '-0', "%Y-W%W-%w")
    print(r)

    if r.year == int(year):
        on_bound = True
        if r.month == int(month) and on_bound:
            on_bound = True
            if 1 <= int(day) <= r.day and on_bound:
                on_bound = True
                print("Date on bound")
            else:
                print("Date not in bound")
                on_bound = False
        else:
            if r.month > int(month):
                on_bound = True
                print("Date on Bound")
            else:
                print("Date not in bound")
                on_bound = False
    else:
        print("Date not in bound")
        on_bound = False
    return on_bound


def cleanup(url):
    url = url.replace("com.", "com")
    url = url.replace(".Vehicle", "/Vehicle")
    url = url.replace("mVehicle", "m/Vehicle")

    return url


# initiate()
import pyautogui as p
import time
import pyperclip
from bs4 import BeautifulSoup as Soup
from CarClass import Car
import datetime

p.FAILSAFE = True
car_list = []


def fetch_data_location():  # Gathers the html code from Copart

    # Open the web browser to obtain the auctions location html code using pyautogui
    p.hotkey('command', 'space')
    p.typewrite("google chrome")
    p.hotkey('enter')
    time.sleep(5)
    p.hotkey('command', 't')
    time.sleep(0.5)
    p.hotkey('command', 'l')
    p.typewrite('https://www.copart.com/auctionCalendar/')
    p.hotkey('enter')
    time.sleep(15)
    p.hotkey('shift', 'command', 'c')
    time.sleep(5)
    p.hotkey('command', 'c')
    s = pyperclip.paste()

    new_html = s

    page_soup = Soup(new_html, "html.parser")
    page_soup.prettify()
    location_soup = page_soup.findAll("li", {"class": "auction-yard-loctaion"})
    for i in range(0, len(location_soup)):
        url = "https://www.copart.com"
        html = str(location_soup[i])
        x = html.find("data-url") + len('data-url"') + 1
        while html[x] != '"':
            url += html[x]
            x += 1

        if url != "https://www.copart.com=":

            url = cleanup(url)
            print(url)
            p.hotkey("command", "w")
            p.hotkey("command", "t")
            fetch_cars_from_auction(url)


def fetch_cars_from_auction(link):  # fetches the car data from a specific auction
    time.sleep(2)
    p.moveTo(1428, 12)
    p.hotkey("command", "l")
    time.sleep(1)
    p.typewrite(link)
    p.hotkey("enter")
    time.sleep(15)
    p.hotkey("shift", "command", "c")
    time.sleep(2)
    # Clicks show all
    p.moveTo(609, 432)
    time.sleep(2)
    p.click()
    p.click()
    time.sleep(8)

    # Copies the code of the table of cars
    p.hotkey("shift", "command", "c")
    time.sleep(2)
    p.moveTo(724, 471)
    time.sleep(2)
    p.click()
    p.click()
    p.click()
    p.hotkey("command", "c")
    p.moveTo(1428, 12)
    s = pyperclip.paste()
    print(s)

    another_new_html = s

    new_soup = Soup(another_new_html, "html.parser")
    new_soup.prettify()

    # Scrape the year
    car_year_soup = new_soup.findAll("span", {"data-uname": "lotsearchLotcenturyyear"})
    indexes = []
    previous_list = len(car_list)
    for i in range(0, len(car_year_soup)):
        year = ""
        strng = str(car_year_soup[i])
        for x in range(43, 47):
            year += strng[x]

        if int(year) >= 2016:
            indexes.append(i)
            car_list.append(Car(year))
            print(strng + " || " + year)

    print("There are " + str(len(indexes)) + " vehicles that are greater than 2016")

    # Scrape the make
    car_make_soup = new_soup.findAll("span", {"data-uname": "lotsearchLotmake"})
    print(car_make_soup)
    c = 0
    while c < len(indexes):
        make = ""
        strng = str(car_make_soup[indexes[c]])
        x = 36
        while strng[x] != "<":
            make += strng[x]
            x += 1
        car_list[c + previous_list].make = make
        print(strng + " || " + make)
        c += 1

    # Scrape the model
    car_model_soup = new_soup.findAll("span", {"data-uname": "lotsearchLotmodel"})
    print(car_model_soup)
    c = 0
    while c < len(indexes):
        model = ""
        strng = str(car_model_soup[indexes[c]])
        print(strng)
        x = 37
        while strng[x] != "<":
            model += strng[x]
            x += 1
        car_list[c + previous_list].model = model
        print(strng + " || " + model)
        c += 1

    # Scrape the damage and bid
    car_damage_soup = new_soup.findAll("tr", {"class": "odd table-row"})
    # Done for every qualifying car
    for i in range(0, len(indexes)):
        strng = str(car_damage_soup[indexes[i]])
        counter = 0
        damage_raw = ""
        damage = ""
        bid_raw = ""
        bid = ""
        # Gets the line where the damage and bid are written
        for y in range(0, len(strng)):
            if strng[y] == "\n":
                counter += 1
            # Damage
            if counter == 60:
                damage_raw += strng[y]

            # Bid
            if counter == 72:
                bid_raw += strng[y]

        # Takes the damage from the line of code
        try:
            x = 7
            while damage_raw[x] != "<":
                damage += damage_raw[x]
                x += 1
            print(damage_raw + " || " + damage)
            car_list[i + previous_list].damage = damage
            # Takes the current bid from the line of code
            x = 39
            while bid_raw[x] != " ":
                bid += bid_raw[x]
                x += 1
            print(bid_raw + " || " + bid)
            car_list[i + previous_list].bid = bid.replace(",", "")
        except IndexError:
            car_list[i + previous_list].damage = "None"
            car_list[i + previous_list].bid = "None"


def cleanup(url):  # Makes the scraped url accessible

    url = url.replace("&amp;", "&")
    url = url.replace(" ", "%20")

    return url


def check_date(date):

    on_bound = True
    now = datetime.datetime.now()
    month = date[5] + date[6]
    day = date[8] + date[9]
    year = date[0] + date[1] + date[2] + date[3]

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


def run():
    print("Started")
    fetch_data_location()

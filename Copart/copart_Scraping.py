import pyautogui as p
import time
import pyperclip
from bs4 import BeautifulSoup as Soup
from CarClass import Car
import datetime

p.FAILSAFE = True  # Failsafe if you want to stop the movements from pyautogui
car_list = []


def fetch_data_location():  # Gathers the html code from Copart

    # Open the web browser to obtain the auctions location html code using pyautogui
    p.hotkey('command', 'space')  # Command for the mac to search for something
    p.typewrite("google chrome")  # Writes whatever is passed as the parameter
    p.hotkey('enter')
    time.sleep(5)  # Waits for google chrome to open
    p.hotkey('command', 't')
    time.sleep(0.5)
    p.hotkey('command', 'l')
    p.typewrite('https://www.copart.com/auctionCalendar/')
    p.hotkey('enter')
    time.sleep(15)
    p.hotkey('shift', 'command', 'c')
    time.sleep(5)
    p.hotkey('command', 'c')
    new_html = pyperclip.paste()  # Pastes HTML code from the clipboard into 'new_html' that will have

    page_soup = Soup(new_html, "html.parser")  # Parses the HTML of new_html
    page_soup.prettify()  # Organizes the containers in page_soup to have them in an HTML syntax.
    # Finds all <li>'s that havve a class called 'auction-yard-location' and adds them to a list called location_soup
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

    time.sleep(2)  # Sets a pause
    p.moveTo(1428, 12)  # Moves the mouse to a specific location of the screen
    p.hotkey("command", "l")  # Command for the mac to search something
    time.sleep(1)
    p.typewrite(link)
    p.hotkey("enter")
    time.sleep(10)
    # Clicks show all
    p.moveTo(827, 351)
    time.sleep(2)
    p.click()  # Click of mouse
    p.click()
    time.sleep(8)
    p.hotkey("shift", "command", "c")  # Opens the inspector of the webpage
    p.click()
    time.sleep(5)
    print("waiting")

    # Copies the code of the table of cars
    p.hotkey("command", "shift", "c")
    p.hotkey("command", "shift", "c")
    time.sleep(2)
    p.moveTo(724, 500)
    time.sleep(2)
    p.click()
    p.hotkey("command", "c")
    p.hotkey("command", "c")
    p.hotkey("command", "c")
    # p.moveTo(1428, 12)
    another_new_html = pyperclip.paste()  # Copy the data from the clipboard into the variable s
    print(another_new_html)

    new_soup = Soup(another_new_html, "html.parser")
    new_soup.prettify()  # Organizes the containers
    print(new_soup)

    # Scrape the year
    car_year_soup = new_soup.findAll("span", {"data-uname": "lotsearchLotcenturyyear"})
    indexes = []
    previous_list = len(car_list)
    print(car_year_soup)
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
    c = 0
    while c < len(indexes):
        model = ""
        strng = str(car_model_soup[indexes[c]])
        x = 37
        while strng[x] != "<":
            model += strng[x]
            x += 1
        car_list[c + previous_list].model = model
        print(strng + " || " + model)
        c += 1

    # Scrape the damage and bid
    # Finds all <td>'s with a class called 'odd table-row' and assigns them to a list called 'car_damage_soup'
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

        # IndexError thrown when the listing is not a car as sometimes the auctions have
        # motorcycles or boats with no damage.
        try:
            x = 7
            while damage_raw[x] != "<":
                damage += damage_raw[x]
                x += 1
            print(damage_raw + " || " + damage)  # This is used to check if the damage was well scraped
            car_list[i + previous_list].damage = damage
            # Takes the current bid from the line of code
            x = 39
            while bid_raw[x] != " ":
                bid += bid_raw[x]
                x += 1
            print(bid_raw + " || " + bid)  # Used for debugging
            car_list[i + previous_list].bid = bid.replace(",", "")  # Removes the
        except IndexError:  # Catches an IndexError and sets the damage and bid to "None"
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
    i = 0
    print("Hello")
    while i < 100:
        print()
        i += 1

    fetch_data_location()

    # run2()


def run2():
    print("It did")
    i = 0
    print("Hello")
    while i < 100:
        print()
        i += 1



#fetch_cars_from_auction("https://www.copart.com/saleListResult/137/2019-02-15?location=FL%20-%20Punta%20Gorda&saleDate=1550242800000&liveAuction=false&from=&yardNum=137")

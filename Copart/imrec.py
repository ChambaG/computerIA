import time
import pyautogui as p
import pyperclip
from bs4 import BeautifulSoup as soup
from CarClass import Car

car_list = []


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
    p.hotkey("command", "c")
    p.moveTo(1428, 12)
    s = pyperclip.paste()

    another_new_html = s
    
    new_soup = soup(another_new_html, "html.parser")
    new_soup.prettify()

    # Scrape the year
    car_year_soup = new_soup.findAll("span", {"data-uname": "lotsearchLotcenturyyear"})
    car_make_soup = new_soup.findAll("span", {"data-uname": "lotsearchLotmake"})
    car_model_soup = new_soup.findAll("span", {"data-uname": "lotsearchLotmodel"})
    car_damage_soup = new_soup.findAll("tr", {"class": "odd table-row"})
    indexes = []
    for i in range(0, len(car_year_soup)):
        year = ""
        strng = str(car_year_soup[i])
        for x in range(43, 47):
            year += strng[x]

        if int(year) >= 2016:

            # Scrape the make
            make = ""
            strng = str(car_make_soup[i])
            x = 36
            while strng[x] != "<":
                make += strng[x]
                x += 1
            print(strng + " || " + make)

            # Scrape the model
            model = ""
            strng = str(car_model_soup[i])
            x = 37
            while strng[x] != "<":
                model += strng[x]
                x += 1
            print(strng + " || " + model)

            # Scrape the damage and bid
            strng = str(car_damage_soup[i])
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
                car_list[i].damage = damage
                # Takes the current bid from the line of code
                x = 39
                while bid_raw[x] != " ":
                    bid += bid_raw[x]
                    x += 1
                print(bid_raw + " || " + bid)
                car_list[i].bid = bid.replace(",", "")
            except IndexError:
                car_list[i].damage = "None"
                car_list[i].bid = "None"


fetch_cars_from_auction("https://www.copart.com/saleListResult/131/2018-12-24?location=FL%20-%20"
                        "Jacksonville%20East&saleDate=1545663600000&liveAuction=false&from=&yardNum=131")

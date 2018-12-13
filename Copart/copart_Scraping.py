import pyautogui as p
import time
import pyperclip
from bs4 import BeautifulSoup as soup
import re
import GUI

cars = []
p.FAILSAFE = True

html = open("Copart/auction_location.txt", "r")
new_html = ""


def fetch_data_location():  # Gathers the html code from Copart
    """"""
    # Open file html.txt for later use

    # Open the web browser to obtain the auctions location html code using pyautoguic
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
    print("opened")
    time.sleep(5)
    p.hotkey('command', 'c')
    print("copied")
    s = pyperclip.paste()



    # Paste the html code from copart into html.txt file
    with open('auction_location.txt', 'w') as g:
        g.write(s)

    new_html = s

    page_soup = soup(new_html, "html.parser")
    page_soup.prettify()
    location_soup = page_soup.findAll("li", {"class":"auction-yard-loctaion"})
    print(str(location_soup))
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
            fetch_cars_from_auction(url)


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


car_html = open("Copart/car_info.txt", "r")


def fetch_cars_from_auction(link):  # fetches the car data from a specific auction
    time.sleep(1)
    p.hotkey("command", "l")
    time.sleep(1)
    p.typewrite(link)
    p.hotkey("enter")
    time.sleep(15)
    try:
        p.locate("Data/showAll.png")
    except:
        pass
    p.hotkey("shift", "command", "c")
    p.hotkey("command", "c")
    print("copied")

    s = pyperclip.paste()

    # Paste the html code from copart into html.txt file
    with open('car_info', 'w') as g:
        g.write(s)

    another_new_html = s

    page_soup = soup(another_new_html, "html.parser")
    page_soup.prettify()
    car_soup = page_soup.findAll("tr", {"class": "row"})
    print(len(car_soup))
    print(str(car_soup))


def cleanup(url):  # Makes the scraped url accessible

    url = url.replace("&amp;", "&")
    url = url.replace(" ", "%20")

    return url


def run():
    print("Started")
    #fetch_data_location()
    for i in range(0, 200000):
        print("Hello: " + str(i))


#  def process_data(): # Gather all the necessary information for each car in an auction

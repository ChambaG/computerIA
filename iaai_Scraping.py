from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import ssl
from CarClass import Car
import datetime
import time
import nn

context = ssl._create_unverified_context()

qualifying_cars_list = []
globavar = 0


def initiate():
    aucLocation_url = 'https://www.iaai.com/locations'
    # Open a connection between the program and IAAI website
    uClient = uReq(aucLocation_url, context=context)
    print("Request successful")
    # Copies the html code into the variable page_html
    page_html = uClient.read()
    print("HTML code read")
    uClient.close()

    page_soup = soup(page_html, "html.parser")
    locations = page_soup.findAll("a", {"class": "detailsLink"})

    # Scrapes the link
    for i in range(0, 3):
        print()
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
    for i in range(0, len(auction_this_day)):
        date = ""
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
            print("Get Cars from auction #" + str(i + 1) + " out of " + str(len(auction_this_day)))
            get_cars(location_url)


def get_cars(url):  # parameter 'url' is the link to a specific auction
    global globavar, qualifying_cars_list
    newclient = uReq(url, context= context)  # Opens the url into the variable newClient
    print("Successful request")
    new_html = newclient.read()  # Assigns the HTML code from 'newclient' to variable 'new_html'
    print("HTML code read correctly")
    newclient.close()  # Closes the connection to the website to save connectivity
    new_soup = soup(new_html, "html.parser")  # Parses the HTML code from 'new_html' into 'new_soup'
    bFound = True
    s = url.find("branchCode=") + 11
    branch = ''
    while bFound:
        strng = url[s]
        if strng == '&':
            bFound = False
        else:
            branch += url[s]

        s += 1

    # Saves all the '<td' containers that hold a class named 'info year' into the list 'car_year_soup'
    car_year_soup = new_soup.findAll("td", {"class": "info year"})
    # A list called 'indexes' that will hold the index of cars that have a year over 2016 in the list 'car_year_soup'
    indexes = []
    for i in range(0, len(car_year_soup)):  # Will pass through each element of 'car_year_soup'
        year = ""
        strng = str(car_year_soup[i])  # 'strng' is equal to the string value of element i in 'car_year_soup'
        for x in range(24, 29):  # Will pass through the characters 24 to 29 to collect the year
            year += str(strng[x])  # 'year' is going to be equal to the year
        if int(year) >= 2016:  # Checks if the year of that car is greater than 2016
            indexes.append(i)  # If true, then the value of i will be added to indexes.

    print("There are " + str(len(indexes)) + " qualifying vehicles in this auction")
    car_list = [Car() for x in range(len(indexes))]  # Creates a list of type Car

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

    # Get the link of the vehicle to later scrape additional information
    # Saves all the '<td' containers that hold a class named 'info secondCol stockNbr' into the list 'car_link'
    car_link = new_soup.findAll("td", {"class": "info secondCol stockNbr"})
    for i in range(0, len(indexes)):  # Passes through every qualifying car of the list 'car_link'
        car_url = "https://www.iaai.com"
        # 'code' is equal to the string value of the element of the integer of indexes[i] in 'car_link'
        code = str(car_link[indexes[i]])
        for x in range(92, 133):  # Passes through the characters 92 to 133 to collect the url
            car_url += code[x]  # 'car_url' is added the characters from 92 to 133 to have the full url of a car
        if car_url.find("/Vehicle?") == -1:  # Corrects a problem with the some cars having shorter url's
            car_url = "https://www.iaai.com"
            for y in range(179, 220):
                car_url += code[y]
        car_list[i].url = cleanup(car_url)  # Adds the complete url to the car in car_list[i]

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

        if bid == "":
            car_list[i].bid = '0'

        elif bid[0] == 'd':
            car_list[i].bid = '0'

        else:
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

        stock_soup = souping.findAll("div", {"id": "promptYes"})

        # Scraping the image
        item_id = ''
        ifound = True
        stock = str(stock_soup)
        s = stock.find('Yesclick(') + 10
        while ifound:
            strng = stock[s]
            if strng == '\'':
                ifound = False
            else:
                item_id += stock[s]

            s += 1

        car_list[i].specific(item_id, branch)

    for i in range(0, len(car_list)):
        car_list[i].qualify()
        car_list[i].qualification = nn.quali(car_list[i].input)
    check = 0
    for i in range(0, len(car_list)):
        if float(car_list[i].qualification) >= 0.00000000001:
            qualifying_cars_list.append(car_list[i])
            print("Added this car to the list final list:")
            car_list[i].show()
            download_image(car_list[i])
            check += 1
            print()
        else:
            print()
            print("This car didnt make it")
            car_list[i].show()

    if check == 0:
        print("No cars were qualified from this auction")


def download_image(car):
    global globavar
    # Scraping the image
    resource = uReq(car.specific_url, context=context)
    filename = "/Users/salvag/Documents/GitHub/computerIA/Images/file" + str(globavar) + ".png"
    output = open(filename, "wb")
    car.filename = filename
    output.write(resource.read())
    output.close()

    globavar = globavar + 1


# Checks if the date of auction is within 2 weeks. Returns true or false. Its parameter is the date of the auction
def check_date(date_of_auction):

    on_bound = True
    now = datetime.datetime.now()  # Uses datetime.now to retreive the current date in the form of MM-DD-YYYY
    today = datetime.datetime.now().day  # gets today's day number

    # Retrieve the month, day and year from the date of the auction
    month = date_of_auction[0] + date_of_auction[1]
    day = date_of_auction[2] + date_of_auction[3]
    year = date_of_auction[4] + date_of_auction[5] + date_of_auction[6] + date_of_auction[7]
    print("Date of the auction: " + str(year) + "-" + str(month) + "-" + str(day))

    # Retrieves the number of the week that we will be in 2 weeks from today (works every day of the year)
    # If this week is number 15 of the year then 'week' will be equal to 17
    week_number = now.date().isocalendar()[1] + 1

    # d is a String that holds the year and week number to be used as a parameter in 'datetime.strptime()'
    d = str(now.year) + "-W" + str(week_number)
    # d = 2019-W6  => where W6 is the number of the week retrieven by line 199 in the year 2019
    # 'limit_date' will hold the date of last day of the week that was specified in line 202
    limit_date = datetime.datetime.strptime(d + '-0', "%Y-W%W-%w")
    # ex: YYYY-MM-DD HH:MM:SS. However, I don't use the time so I don't use that part.
    print("Limit date: " + str(limit_date))

    if limit_date.year == int(year):  # First compare the year for limit_day to the year of the auction
        on_bound = True
        if limit_date.month == int(month) and on_bound:  # If the auction happens in the same month from limit_date...
            on_bound = True
            # Check if the auction happens: before the last day of the limit_date or today
            if 1 <= int(day) <= limit_date.day and on_bound and (int(day) != int(today)):
                on_bound = True
                print("Date on bound")
            else:
                print("Date not in bound")
                on_bound = False
        else: # Check if the month of the auction is before the month of limit_date and if the auction day is today
            if limit_date.month > int(month) and (int(day) != int(today)):
                on_bound = True
                print("Date on Bound")
            else:  # If the month is after the month of limit_date dismiss this auction
                print("Date not in bound")
                on_bound = False
    else:  # If the year is different dismiss this auction and skip the nested if's
        print("Date not in bound")
        on_bound = False
    return on_bound  # Return either true or false


def cleanup(url):
    url = url.replace("com.", "com")
    url = url.replace(".Vehicle", "/Vehicle")
    url = url.replace("mVehicle", "m/Vehicle")

    return url

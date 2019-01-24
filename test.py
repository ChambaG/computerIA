import datetime

url = "https://www.copart.com/saleListResult/86/2019-01-23?location=FL%20-%20Ft.%20Pierce&saleDate=1548255600000&liveAuction=false&from=&yardNum=86"

date = ""
i = url.find("?location") - 1
while url[i] != "/":
    date += url[i]
    i -= 1

date = date[::-1]
date = "2019-02-13"


def check_date(date):

    print(date)
    on_bound = True
    now = datetime.datetime.now()
    month = date[5] + date[6]
    day = date[8] + date[9]
    year = date[0] + date[1] + date[2] + date[3]
    print(year)

    week = now.date().isocalendar()[1] + 1

    d = str(now.year) + "-W" + str(week)
    # Limit date
    r = datetime.datetime.strptime(d + '-0', "%Y-W%W-%w")
    print(r)

    if r.year == int(year):
        on_bound = True
        if r.month == int(month) and on_bound:
            on_bound = True
            print("yes")
            if 1 <= int(day) <= r.day and on_bound:
                on_bound = True
                print("Date on bound")
            else:
                print("Date not in bound")
                on_bound = False
        else:
            if r.month > int(month):
                on_bound = True
                print("yes")

                print("Date on Bound")
            else:
                print("Date not in bound")
                on_bound = False
    else:
        print("Date not in bound")
        on_bound = False
    return on_bound


print(check_date(date))
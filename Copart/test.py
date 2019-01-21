import datetime

on_bound = True
now = datetime.datetime.now()
month = "01"
day = "10"
year = "2019"

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

print(on_bound)


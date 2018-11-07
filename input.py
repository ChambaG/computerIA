

class Car:

    def __init__(self):
        self.year = 0
        self.make = ""
        self.model = ""
        self.damage = ""


training_cars = [Car() for i in range(0, 300)]

file = open('training_data.txt', 'r')

for i in range(0, 300):
    line = file.readline()

    # Takes the year out of the text
    year = ""
    for x in range(0, 4):
        year += line[x]

    training_cars[i].year = int(year)

    # Takes the make out of the text
    make = ""
    model = ""
    damage = ""
    x = 5
    while x < len(line):
        letter = line[x]
        if letter == " ":
            x = len(line)
        else:
            make += letter
        x += 1
    training_cars[i].make = make
    y = 4 + len(training_cars[i].make) + 2

    w = 2

    while y < len(line):
        letter = line[y]
        if letter == "|":
            w += y
            y = len(line)
        else:
            model += letter
        y += 1
    training_cars[i].model = model

    while w < len(line):
        letter = line[w]
        damage += letter
        w += 1

    training_cars[i].damage = damage

    print("iteration: " + str(i + 1))
    print(training_cars[i].year)
    print(training_cars[i].make)
    print(training_cars[i].model)
    print(training_cars[i].damage)

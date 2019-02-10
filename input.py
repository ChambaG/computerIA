from CarClass import Car

training_cars = [Car() for i in range(0, 30)]  # Create a list of type Car with 700 elements
file = open('training_data.txt', 'r')  # Read the file 'training_data.txt'

for i in range(0, 29):  # Repeat for each entry in the list
    line = file.readline()

    # Takes the year out of the text
    year = ""
    for x in range(0, 4):
        year += line[x]

    print(year)

    training_cars[i].year = int(year)  # Add the year to the object

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
    training_cars[i].make = make  # Add the make to the object
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
    training_cars[i].model = model  # Add the model to the object

    while w < len(line):
        letter = line[w]
        damage += letter
        w += 1

    training_cars[i].damage = damage.replace('\n', '')  # Add the damage to the object

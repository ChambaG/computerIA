import pyautogui
import time
import re
import os

cars = []
pyautogui.FAILSAFE = True


class Car:

    def __init__(self):
        self.year = ""
        self.make = ""
        self.model = ""
        self.bid = 0
        self.damage = ""
        self.lot_id = 0
        self.url = ("./lot/" + str(self.lot_id) + "/Photos")


def fetch_data():
    pyautogui.hotkey('command', 'tab')
    time.sleep(1)
    # <editor-fold desc="First Indent">
    
    # </editor-fold>
    pyautogui.click(744, 356, button='right')  # Right clicks to pop the inspector
    pyautogui.moveRel(54, 225, duration=0.5)  # Move to Open inspector
    pyautogui.click(button='left')
    pyautogui.click(1049, 457, button='left', duration=3)  # First indent
    pyautogui.moveTo(1060, 549, duration=0.5)  # Second indent
    pyautogui.click(button='left')
    pyautogui.moveTo(1105, 505, duration=0.5)  # Body indent
    pyautogui.click(button='right')
    pyautogui.hotkey('command', 'c')
    time.sleep(2)

    pyautogui.hotkey('command', 'space')
    pyautogui.typewrite('sample.txt')
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('command', 'a')
    pyautogui.hotkey('command', 'v')
    pyautogui.hotkey('command', 's')
    pyautogui.hotkey('command', 'tab')
    time.sleep(2)


def process_data():
    # Opens the file of the processed HTML code
    file = open('sample._lcNrD.txt', 'r')

    line = file.readline()
    file_list = []
    file_list2 = []
    file_list.append([])
    file_list[0].append(line)

    count = 0
    for line in file:
        count += 1
        file_list.append([])
        file_list[count].append(line)

    # Create object of type Car inside the elements of the car_list list
    car_list = [Car() for i in range(0, (count + 1))]

    count += 1
    print("There are " + str(count) + " in this auction")

    for i in range(0, count):

        srt_len = 6 + len(car_list[i].make)
        space_found = False
        space_counter = 0


        # 2018 MITSUBISHI OUTLANDER XE
        if car_list[i].make == "MITSUBISHI":
            while space_counter != 2:
                if lot_desc[srt_len] == " ":
                    space_counter += 1
                    car_list[i].model += lot_desc[srt_len]
                    srt_len += 1
                else:
                    car_list[i].model += lot_desc[srt_len]
                    srt_len += 1

            str1 = re.compile(car_list[i].model)
            print(str1)
            r = str1.search('SPORT ')


        elif car_list[i].make == "JEEP":
            while space_counter != 2:
                if lot_desc[srt_len] == " ":
                    space_counter += 1
                    car_list[i].model += lot_desc[srt_len]
                    srt_len += 1
                else:
                    car_list[i].model += lot_desc[srt_len]
                    srt_len += 1
        else:
            while not space_found:
                if lot_desc[srt_len] == " ":
                    space_found = True
                else:
                    car_list[i].model += lot_desc[srt_len]
                    srt_len += 1

        

        # </editor-fold>

        # <editor-fold desc="Lot iD">
        keyword = re.compile("lot-id=")
        r = keyword.search(str(file_list[i]))
        inx = r.end() + 1
        line2 = str(file_list[i])
        id = ""
        while line2[inx] != '"':
            id += line2[inx]
            inx += 1
        car_list[i].lot_id = id
        # </editor-fold>

        # <editor-fold desc="Lot Bid">
        keyword = re.compile("current-bid=")
        r = keyword.search(str(file_list[i]))
        inx = r.end() + 1
        line2 = str(file_list[i])
        bid = ""
        while line2[inx] != '"':
            bid += line2[inx]
            inx += 1
        car_list[i].bid = bid
        # </editor-fold>

    # <editor-fold desc="Lot Damage">
    sample = open('sample.txt', 'r')
    line2 = sample.readline()
    file_list2.append([])
    file_list2[0].append(line2)

    count2 = 0
    count3 = 0
    div_list = []
    for line2 in sample:
        count2 += 1
        file_list2.append([])
        file_list2[count2].append(str(line2))
        if str(file_list2[count2]) == ("['                    </div>" + "\\" + "n']"):
            div_list.append(count2)
            count3 += 1

    for i in range(0, count):
        damage = ""
        pattern = re.compile("<span>")
        r = pattern.search(str(file_list2[div_list[i] + 20]))
        index = r.end()
        string = str(file_list2[div_list[i] + 20])
        while string[index] != "<":
            damage += string[index]
            index += 1

        car_list[i].damage = damage

    return car_list
    # </editor-fold>



def process_copart():
    file = open('sample2.txt', 'r')
    line = file.readline()
    car_count = 0
    while line != "DONE":
        line = file.readline()
        car_count += 1

    checkCar_list = [Car() for i in range(0, car_count)]

    i = 0
    line2 = file.readline()
    print(line2)
    print("Done")
    """
    while line2 != "DONE":
        line2 = file.readline()
        # Year
        year = ""
        for x in range(90, 95):
            year += line2[x]

        checkCar_list[i].year = int(year)
        # Model
        # Make
        # iD
        # Bid
    """
    file = open('sample.txt', 'r')
    line = file.readline()
    # Damage
    print(checkCar_list[i].year)

def remove_spaces():
    file = open('sample.txt', 'r')
    temp = open('temporary_file.txt', 'w+')

    for line in file:
        if '<' in line:
            temp.write(line)

    os.replace('temporary_file.txt', 'sample.txt')


def run():
    # fetch_data()
    # remove_spaces()
    process_copart()


run()

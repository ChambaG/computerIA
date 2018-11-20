import pyautogui as p
import time
import re
import os
import pyperclip

cars = []
p.FAILSAFE = True


def fetch_data():
    # Opening
    html = open("html.txt", "w+")
    p.hotkey('command', 'space')
    p.typewrite("google chrome")
    p.hotkey('enter')
    time.sleep(5)
    p.hotkey('command', 't')
    time.sleep(0.5)
    p.hotkey('command', 'l')
    p.typewrite('https://www.copart.com/auctionCalendar/')
    p.hotkey('enter')
    time.sleep(5)
    p.hotkey('shift', 'command', 'c')
    time.sleep(5)
    p.hotkey('command', 'c')
    s = pyperclip.paste()
    with open('auction_location.txt', 'w') as g:
        g.write(s)




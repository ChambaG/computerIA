import pyautogui, time

time.sleep(0)

coord = pyautogui.locateOnScreen('/Users/salvag/PycharmProjects/auto/Data/x.png', 0.5)
x, y = pyautogui.center(coord)
print(str(x/2) + " " + str(y/2))
pyautogui.moveTo((x/2), (y/2))
#pyautogui.click()

#pyautogui.moveTo(100, 901)
print(pyautogui.position())

try:
    coord = pyautogui.locateOnScreen('/Users/salvag/PycharmProjects/auto/Data/testing.png', 0.8)
    x, y = pyautogui.center(coord)
    print(str(x/2) + " " + str(y/2))
    pyautogui.moveTo((x/2), (y/2))
    pyautogui.click()
except KeyboardInterrupt:
    print("Nothing wil happen")
except TypeError:
    print("Nothing will happen")

#pyautogui.moveTo(100, 901)
print(pyautogui.position())


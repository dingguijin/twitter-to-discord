import pyautogui
import time
import datetime

def monitor_chrome():
    titles = pyautogui.getAllTitles()
    
    print(datetime.datetime.now())
    print(titles)

    for title in titles:
        if "Chrome" in title:
            window = pyautogui.getWindowsWithTitle(title)[0]
            window.activate()

            #if pyautogui.locateOnScreen('error.png', grayscale=True, confidence=0.9) is not None:
            #    print("Something went wrong while displaying this page.")
            pyautogui.hotkey('ctrl', 'r')


monitor_chrome()


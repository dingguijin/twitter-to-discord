import pyautogui
import time

def monitor_chrome():
    while True:
        titles = pyautogui.getAllTitles()
        for title in titles:
            if "Chrome" in title:
                window = pyautogui.getWindowsWithTitle(title)[0]
                window.activate()

                #if pyautogui.locateOnScreen('error.png', grayscale=True, confidence=0.9) is not None:
                #    print("Something went wrong while displaying this page.")
                pyautogui.hotkey('ctrl', 'r')

        time.sleep(600)

monitor_chrome()


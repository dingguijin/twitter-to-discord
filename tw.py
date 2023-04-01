from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui as ag

def up_down(driver):
    ag.moveTo(800, 600)
    ag.scroll(100)
    ag.scroll(-100)
    return

def get_driver_instance():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    return driver

def get_page(driver, url):
    driver.get(url)
    title = driver.title
    print(title)
    driver.implicitly_wait(2.0)
    time.sleep(1.0)
    time.sleep(10)
    while True:
        try:
            frame = driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-jxzhtn.r-1ljd8xs.r-13l2t4g.r-1phboty.r-16y2uox.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > section > div > div > div:nth-child(1) > div > div > div > div > span")
        except Exception as e:
            time.sleep(10)
            up_down(driver)
            continue
        if frame:
            print(frame)
            frame.click()
            time.sleep(10)
            up_down(driver)


    return


if __name__ == "__main__":
    driver = get_driver_instance()
    url = "https://twitter.com/home"
    s = get_page(driver, url)

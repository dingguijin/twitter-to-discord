from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.chrome.service import Service as ChromeService

import os
import sys
import time
import random
import pyautogui as ag


def restart():
    os.execv(sys.executable, ['python'] + sys.argv)
    return

def print_tweet(driver):
    es = driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
    if not es:
        return
    for e in es:
        _t = e.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetText"]')
        print(_t)
        print(_t.text)
        print(_t.id)
    return

def scroll_with_se(driver, offset):
    time.sleep(1)
    driver.execute_script('return window.scrollTo(0, %d);' % offset)
    print_tweet(driver)
    return

def up_down_with_se(driver):
    scroll_with_se(driver, 12)
    time.sleep(2);
    for i in range(10):
        y = (i+1) * 1280
        scroll_with_se(driver, y)
        _t = random.gauss(4.0, 3.5)
        time.sleep(abs(_t));

    scroll_with_se(driver, 12)
    ele = driver.find_element(By.XPATH, "//*[@id=\"react-root\"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[1]")
    if ele:
        ele.click()
    return

def get_driver_instance():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    return driver

def find_articles(driver):
    body = driver.find_element_by_tag_name('body')
    for i in range(3):
        body.send_keys(Keys.END)
        time.sleep(5)

    posts = driver.find_elements(By.CSS_SELECTOR, 'article')
    if not posts:
       return None 

    for post in posts:
        username = post.find_element(By.CSS_SELECTOR, 'span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0')
        user_id = post.find_element(By.CSS_SELECTOR, 'a.css-4rbku5.css-18t94o4.css-1dbjc4n.r-kemksi.r-wgabs5.r-1loqt21.r-1pi2tsx.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af.r-o7ynqc.r-6416eg').get_attribute('href').split('/')[-1]
        content = post.find_element(By.CSS_SELECTOR, 'div.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0').text
        content_id = post.get_attribute("data-testid")
        print(f"Username: {username.text}")
        print(f"User ID: {user_id}")
        print(f"Content: {content}")
        print(f"Content ID: {content_id}")

    return None

def get_page(driver, url):
    driver.get(url)
    title = driver.title
    print(title)
    driver.implicitly_wait(2.0)
    time.sleep(1.0)
    time.sleep(10)
        #frame = driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-jxzhtn.r-1ljd8xs.r-13l2t4g.r-1phboty.r-16y2uox.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > section > div > div > div:nth-child(1) > div > div > div > div > span")
    articles = find_articles(driver)
    if not articles:
        raise Exception("No Articles")
    time.sleep(abs(random.gauss(10.0, 8.0)))
    raise Exception("Restart")
    return


if __name__ == "__main__":
    driver = get_driver_instance()
    url = "https://twitter.com/home"
    try:
        s = get_page(driver, url)
    except Exception as e:
        print(e)
        restart()

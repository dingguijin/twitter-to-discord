from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys


import os
import sys
import time
import random
import pyautogui as ag

import redis
import hashlib
import json

# 建立 Redis 连接
client = redis.Redis(host='localhost', port=6379)

def save_tweet_to_queue(username, user_id, content):
    user_hash = hashlib.sha256(f"{username}{user_id}{content}".encode()).hexdigest()
    key_exists = client.exists(user_hash)
    if not key_exists:
        client.set(user_hash, '')
        user_dict = {'username': username, 'user_id': user_id, 'content': content}
        client.lpush('tweet_queue', json.dumps({user_hash: user_dict}))
        print(f"New user {username} created with tweet: {content}")

#save_tweet_to_queue("John", "123456", "Hello World!")


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

def parse_posts(driver, posts):
    _username_css = "a.css-4rbku5.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1wbh5a2.r-dnmrzs.r-1ny4l3l div div span.css-901oao.css-16my406.css-1hf3ou5.r-poiln3.r-bcqeeo.r-qvutc0 span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0"
    _id_css = "div.css-1dbjc4n.r-18u37iz.r-1wbh5a2.r-13hce6t > div.css-1dbjc4n.r-1d09ksm.r-18u37iz.r-1wbh5a2 > div.css-1dbjc4n.r-1wbh5a2.r-dnmrzs > a.r-1ny4l3l > div > span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0"

    _content_css = "div[data-testid=\"tweetText\"] > span"
    for post in posts:
        username = post.find_element(By.CSS_SELECTOR, _username_css).text
        user_id = post.find_element(By.CSS_SELECTOR, _id_css).text
        content = post.find_element(By.CSS_SELECTOR, _content_css).text
        content_id = post.get_attribute("data-testid")
        print(f"Username: {username.text}")
        print(f"User ID: {user_id}")
        print(f"Content: {content}")
        print(f"Content ID: {content_id}")
        save_tweet_to_queue(str(username), str(user_id), str(content))

def find_articles(driver):
    body = driver.find_element(By.TAG_NAME, 'body')
    for i in range(3):
        posts = driver.find_elements(By.CSS_SELECTOR, 'article')
        if not posts:
            continue
        parse_posts(driver, posts)
        body.send_keys(Keys.END)
        time.sleep(1.5)
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
    return


if __name__ == "__main__":
    driver = get_driver_instance()
    url = "https://twitter.com/home"

    while True:
        get_page(driver, url)

from selenium import webdriver
from time import sleep
from info import username, password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()
driver.get("https://www.instagram.com/")
sleep(5)
driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_css_selector(".L3NKy").click()
sleep(5)
driver.get("https://www.instagram.com/"+username)


def getFollows():
    driver.find_element_by_css_selector(
        "li.Y8-fY:nth-child(3) > a:nth-child(1)").click()
    sleep(5)
    followingCount = driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span")
    sayac = 1
    pyautogui.click(x=840, y=443)
    while sayac <= int(followingCount.text):
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "FPmhX.notranslate._0imsa")))
            follows_elems = driver.find_elements_by_class_name(
                "FPmhX.notranslate._0imsa")
        except TimeoutException:
            print("Loading took too much time!")
        sayac += 1
        if sayac % 3 == 0:
            pyautogui.scroll(-1000)
            sleep(0.5)
    else:
        followList = []
        sayac2 = 1
        for e in follows_elems:
            x = e.text
            followList.append(x)
            sayac2 += 1
        pyautogui.click(x=1000, y=443)
        return followList


def getFollowers():
    driver.find_element_by_css_selector(
        "li.Y8-fY:nth-child(2) > a:nth-child(1)").click()
    sleep(5)
    followerCount = driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span")
    sayac = 1
    pyautogui.click(x=840, y=443)
    while sayac <= int(followerCount.text):
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "FPmhX.notranslate._0imsa")))
            followers_elems = driver.find_elements_by_class_name(
                "FPmhX.notranslate._0imsa")
        except TimeoutException:
            print("Loading took too much time!")
        sayac += 1
        if sayac % 3 == 0:
            pyautogui.scroll(-1000)
            sleep(0.5)
    else:
        followerList = []
        sayac2 = 1
        for e in followers_elems:
            x = e.text
            followerList.append(x)
            sayac2 += 1
        pyautogui.click(x=1000, y=443)
        return followerList


followsList2 = getFollows()
sleep(1)
followerList2 = getFollowers()

for follow in followsList2:
    if follow not in followerList2:
        print(follow)

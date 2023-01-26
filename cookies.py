from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import sys

sys.setrecursionlimit(1000000000)


CHROME_DRIVER = "./chromedriver"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(executable_path=CHROME_DRIVER, log_path="NUL"))
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie_x_path = '//*[@id="cookie"]'

cookie = driver.find_element(By.XPATH, cookie_x_path)

timeout = time.time() + 5

while True:
    cookie.click()

    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR,"#store b")

        item_prices = []
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        money = driver.find_element(By.ID, "money")

        if "," in money.text:
            money = money.text.replace(",", "")
            money = int(money)
        else:
            money = int(money.text)

        

        for num in item_prices:
            if num <= money:
                chosen_upgrade = num
        

        x_paths = ['//*[@id="buyCursor"]', '//*[@id="buyGrandma"]','//*[@id="buyFactory"]','//*[@id="buyMine"]', '//*[@id="buyShipment"]','//*[@id="buyAlchemy lab"]', '//*[@id="buyPortal"]','//*[@id="buyTime machine"]']
        
        index = item_prices.index(chosen_upgrade)
        to_click = x_paths[index]

        icon = driver.find_element(By.XPATH, to_click)
        icon.click()
        print("clicked")
        timeout = time.time() + 5
    

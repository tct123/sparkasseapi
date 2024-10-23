from fastapi import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

load_dotenv()
URL = os.getenv("URL")
NAME = os.getenv("NAME")
PASSWORD = os.getenv("PASSWORD")

browser = webdriver.Firefox()
browser.get(URL)
loginbtn1 = browser.find_element(
    By.XPATH, "/html/body/div/div[2]/div/div[4]/form/button"
)
loginbtn1.click()
usernamefield = browser.find_element(By.XPATH, '//*[@id="KrtsifzaAFgaSpmL"]')
usernamefield.send_keys(NAME, Keys.ENTER)
time.sleep(1)
passwordfield = browser.find_element(By.XPATH, '//*[@id="sHVFpWLsENRUTCom"]')
passwordfield.send_keys(PASSWORD, Keys.ENTER)

continuebtn = browser.find_element(By.XPATH, '//*[@id="defaultAction"]')
continuebtn.click()
accountbalance = browser.find_element(
    By.XPATH, "/html/body/div/section/div/div/div[4]/form/div[3]/div/div[3]/div/span[3]"
)
print(accountbalance.text)
# END Browser
browser.quit()

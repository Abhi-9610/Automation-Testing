from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from const import *

driver = webdriver.Firefox()


def driver_url(url):
    driver.get(url)
    WebDriverWait(driver, 10)

def click(by, locator):
    try:
        element = driver.find_element(by, locator)
        element.click()
    except Exception as e:
        print(f"An error occurred while trying to click the element: {e}")

def input(by, locator, text):
    element = driver.find_element(by, locator)
    element.send_keys(text) 

def upload(by, locator, path):
    element = driver.find_element(by, locator)
    element.send_keys(path)



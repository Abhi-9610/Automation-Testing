from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

def browser(url):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body"))) 
def click(by, locator):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, locator)))
    element.click()
    return element 

def input_field(by, locator, text):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, locator)))
    element.clear()  
    element.send_keys(text)

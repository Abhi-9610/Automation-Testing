import json
from selenium import webdriver
from const import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver=webdriver.Firefox()

def link(url):
    driver.get(url)

def inputs(by, locator, value):
    
    k=WebDriverWait(driver, 10).until(ec.element_to_be_clickable((by, locator)))
    k.send_keys(value)

def button(by , locator):
    element= WebDriverWait(driver, 10).until(ec.element_to_be_clickable((by, locator)))
    element.click()
    return True

def check(by, locator):
    
        k = WebDriverWait(driver, 10).until(ec.presence_of_element_located((by, locator)))
        print(k.text)  
        return k.text  
def store_cookies(filename='cookies.json'):
    cookies = driver.get_cookies()
    with open(filename, 'w') as file:  
        json.dump(cookies, file) 
        
def load_cookies(filename='cookies.json'):
    try:
        with open(filename, 'r') as file: 
            cookies = json.load(file) 
            for cookie in cookies:
                driver.add_cookie(cookie) 
        driver.refresh() 
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the cookie file.")
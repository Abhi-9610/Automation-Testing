from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import json  # Import json to handle file operations

driver = webdriver.Firefox()
driver.get("https://www.amazon.in/")

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

def account_hover():
    try:
        hover_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@id='nav-link-accountList']"))
        )
        ActionChains(driver).move_to_element(hover_element).perform()
    except Exception as e:
        print(f"Error during account hover: {e}")
    
def click_wishlist():
    try:
        wishlist_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Create a Wish List']"))
        )
        wishlist_button.click() 
    except Exception as e:
        print(f"Error clicking wishlist button: {e}")
    
def click_create_wishlist():
    try:
        create_wishlist_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='createList']"))
        )
        create_wishlist_button.click()      
    except Exception as e:
        print(f"Error clicking create wishlist button: {e}")
    
def input_wishlist_name(name):
    try:
        wishlist_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='list-name']"))
        )
        wishlist_name_input.clear() 
        wishlist_name_input.send_keys(name) 
    except Exception as e:
        print(f"Error inputting wishlist name: {e}")
    
def click_create_button():
    try:
        create_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@class='a-button-input a-declarative']")) 
        )
        create_button.click()   
        driver.refresh()
        WebDriverWait(driver, 15)

    except Exception as e:
        print(f"Error clicking create button: {e}")

load_cookies()
account_hover()
click_wishlist()
click_create_wishlist()
input_wishlist_name("My Wishlist")
click_create_button()
driver.quit()

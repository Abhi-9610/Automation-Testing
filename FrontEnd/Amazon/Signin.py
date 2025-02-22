from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import json  # Import json to handle file operations

driver = webdriver.Firefox()
driver.get("https://www.amazon.in/")

def account_hover():
    signin_hover = driver.find_element(By.XPATH, "//a[@id='nav-link-accountList']")
    ActionChains(driver).move_to_element(signin_hover).perform()

def click_signin_button():
    signin_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='nav-action-inner']"))
    )
    signin_button.click()

def input_email(email):
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='ap_email']"))
    )
    email_input.send_keys(email)

    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='continue']"))
    )
    continue_button.click()

def input_password(password):
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='ap_password']"))
    )
    password_input.send_keys(password)

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='signInSubmit']"))
    )
    submit_button.click()

def store_cookies(filename='cookies.json'):
    cookies = driver.get_cookies()
    with open(filename, 'w') as file:  
        json.dump(cookies, file)  

account_hover()
click_signin_button()
input_email("9610abhisingh@gmail.com")
input_password("1Billion$")
store_cookies() 

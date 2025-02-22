from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://www.amazon.in/")

def account_hover():
    hover_element = driver.find_element(By.XPATH, "//a[@id='nav-link-accountList']")
    ActionChains(driver).move_to_element(hover_element).perform()

def click_signup_button():
    signup_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Start here.')]"))
    )
    signup_button.click()

def input_email(email):
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='ap_email']"))
    )
    email_input.send_keys(email)

def input_name(name):
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='ap_customer_name']"))
    )
    name_input.send_keys(name)

def input_mobile(mobile):
    mobile_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='ap_phone_number']"))
    )
    mobile_input.send_keys(mobile)

def input_password(password):
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='ap_password']"))
    )
    password_input.send_keys(password)

def verify_mobile_number():
    verify_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='continue']"))
    )
    verify_button.click()

account_hover()
click_signup_button()
# input_email("vermaxabhi02@gmail.com")  //uncomment this line to use email
input_name("Abhishek Singh")
input_mobile("9610927173")
input_password("1Billion$")
verify_mobile_number()

from selenium.webdriver.common.by import By
import random


by=By.XPATH

url="https://www.saucedemo.com/"
username="//input[@id='user-name']"
password= "//input[@id='password']"
login_button="//input[@id='login-button']"
error="//h3[@data-test='error']"

usr=["standard_user", "locked_out_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"]
name= random.choice(usr)
print(name)
pswrd="secret_sauce"    

cart="//a[@class='shopping_cart_link']"
addtocart="//button[@data-test='add-to-cart-sauce-labs-backpack']"
title="//a[@id='item_4_title_link']"
price="//div[@class='inventory_item_price']"
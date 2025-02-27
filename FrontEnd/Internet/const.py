from selenium.webdriver.common.by import By

by = By.XPATH
url = "https://the-internet.herokuapp.com/upload"
upload_button = "//input[@id='file-upload']"  
name = r"C:\Users\av293\OneDrive\Documents\new.html"
submit_button="//input[@id='file-submit']"
error = "//html/body/h1"


# Uploading files with wrong file extension
wrong_file_extension = r"C:\Users\av293\OneDrive\Documents\new.txt"

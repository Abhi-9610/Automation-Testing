import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from const import *
from helper import *


link(url)

# using correct email and password
def success():
   
    inputs(by,username,name)
    inputs(by, password,pswrd)
    button(by,login_button)
    
#using incorrect password and correct mail
def incorrect():
    inputs(by,username,name)
    inputs(by,password,"secret_sauce1")
    button(by,login_button)
    res=check(by,error)
    if res == "":
        print("Login Successful")
    else:
        print("Login failed")
 


#using incorrect email and password
def incorrect_mail():
    inputs(by,username,"1@mailinator.com")
    inputs(by,password,"secret_sauce1")
    button(by,login_button)
    res=check(by,error)
    if res == "":
        print("Login Successful")
    else:
        print("Login failed")

success()
store_cookies()
driver.quit()
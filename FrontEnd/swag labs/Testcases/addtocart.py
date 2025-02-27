import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from const import *
from helper import *


link(url)
load_cookies()

# Adding Product to cart
def adding():
    button(by,addtocart)
    print(check(by,title),check(by,price))

adding()
driver.quit()

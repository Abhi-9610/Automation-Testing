import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helper import *
from const import *

driver_url(url)
click(by, navbutton)
click(by, upload_button)


def not_working():
    click(by, file_upload)
    upload(by, file_upload, r"C:\Users\av293\OneDrive\Pictures\dp.png")
  
 

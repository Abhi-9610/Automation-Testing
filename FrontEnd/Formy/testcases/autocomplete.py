import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helper import *
from const import *

driver_url(url)
click(by, navbutton)
click(by, upload_button)
upload(by, file_upload, name)
  
 

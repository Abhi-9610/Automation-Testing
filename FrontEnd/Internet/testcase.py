import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helper import *
from const import *


browser(url)

#success case:----
try:
    input_field(by, upload_button, name)
    print("Upload button clicked successfully!")
    click(by,submit_button)
except Exception as e:
    print(f"Error clicking upload button: {e}")

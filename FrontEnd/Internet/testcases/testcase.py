import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helper import *
from const import *

browser(url)

# Ensure the file uploading window of PC is open and then upload the file
def upload_file():
    try:
        click(by, upload_button)  
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, upload_button)))  
        input_field(by, upload_button, name)  
        print("File upload initiated successfully!")
        click(by, submit_button) 
    except Exception as e:
        print(f"Error during file upload: {e}")

# Clicking on submit without uploading
def clicking_on_submit_without_uploading():
  
        click(by, submit_button)
        print("Submit button clicked successfully!")
        error_message = driver.find_element(by, error)
        print(error_message.text)  

# Uploading files with wrong file extension         
def uploading_files_with_wrong_file_extension():
    try:
        input_field(by, upload_button, wrong_file_extension)  
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, upload_button)))
        print("File upload initiated successfully!")
        click(by, submit_button)  
    except Exception as e:
        print(f"Error during file upload: {e}")

# upload_file()
# clicking_on_submit_without_uploading()
uploading_files_with_wrong_file_extension()

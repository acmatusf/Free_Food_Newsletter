#install newest version of python, and pip (pip is a package manager to install python library)
#pip install selenium
#pip install webdriver-manager

#!!!!!!!!!!!!!!

# To run the script, type in the terminal: python3 scrape_selenium.py
# Also, to run any python file, remember to type in the terminal: python3 <filename.py>

#!!!!!!!!!!!!!!

from selenium import webdriver # Webdriver is used to control the browser (open, click button, fill information), example of web brower: Chrome, Firefox, Safari, Edge
from selenium.webdriver.chrome.service import Service as ChromeService # In this case we use the Chrome Service
from webdriver_manager.chrome import ChromeDriverManager # We use the ChromeDriverManager to ensure that the right version of Chrome is used (used to update the correct version)
from selenium.webdriver.common.by import By # By is used to locate elements on the page, for example, when you inspect any webbrower, you can see the elements on the page (html code), and a block of code will have id or class to classifies them(example: class="list-group-item")

import time # Time is used to give time to the chrome to appear

#Set up the Webdriver and open chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Open the URL
driver.get("https://bullsconnect.usf.edu/events?topic_tags=7276307")
#Time the chrome gonna be appear, in this case 40 seconds
time.sleep(40)

#!!!!!!!!!!!!!!!!!!!

#We can not by pass the 2 factor authentication from usf account so we have to manually log in in this case. 40 seconds is enough time to log in, depend on your need you can change the time

#!!!!!!!!!!!!!!!!!!!

# Find all <li> tags with the class "list-group-item"
event_items = driver.find_elements(By.CLASS_NAME, "list-group-item")


# Open the text file in write mode
with open("content.txt", "w") as f:
    for item in event_items:
        # Writing content to the file, in this case, event details are scraped as HTML code, so we have to translate them to text before writing them to the file
        f.write(item.text)

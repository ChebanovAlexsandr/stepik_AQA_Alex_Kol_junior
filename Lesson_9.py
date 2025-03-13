import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys

options = Options()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

INPUT = ("css selector", 'input#target')

driver.get("https://the-internet.herokuapp.com/key_presses")
time.sleep(3)
driver.find_element(*INPUT).send_keys(Keys.ENTER+Keys.CONTROL)
time.sleep(3)
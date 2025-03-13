import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

options = Options()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
action = ActionChains(driver)
wait = WebDriverWait(driver, 10, poll_frequency=1)

INPUT = ("xpath", '(//input[@type="text"])[1]')
HOME = ('xpath', '//*[@id="header"]/nav/div/div[2]/ul/li[1]/a')

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
driver.execute_script("alert('Hello, Selenium!');")
time.sleep(3)
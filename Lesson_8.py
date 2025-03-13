from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://demoqa.com/selectable")

GRID = ("xpath", '//*[@id="demo-tab-grid"]')
ONE = ("css selector", '#row1 > li:nth-child(1)')

driver.find_element(*GRID).click()
one = driver.find_element(*ONE)
assert one.is_selected() == False,"Кнопка активна"
one.click()
assert one.is_selected() == True, "Кнопка не активна"
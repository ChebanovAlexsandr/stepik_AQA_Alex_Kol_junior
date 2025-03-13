from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

INPUT = ("xpath", '(//input[@type="text"])[1]')
HOME = ('xpath', '//*[@id="header"]/nav/div/div[2]/ul/li[1]/a')

driver.get("https://demo.automationtesting.in/Frames.html")

driver.switch_to.frame("singleframe")

driver.find_element(*INPUT).send_keys("Писька")

driver.switch_to.default_content()

driver.find_element(*HOME).click()
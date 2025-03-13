import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")

wait = WebDriverWait(driver, 10, poll_frequency=1)

NO_VISIBLE_TEXT = ("xpath", '//*[@id="deletesuccess"]')
BUTTON_TEXT = ('xpath', '//*[@id="alert2"]')

INVVIB_TEXT = ('xpath', '//*[@id="delayedText"]')

ENEBLET = ('xpath', '//*[@id="timerButton"]')

DESEBLET = ('xpath','//*[@id="myBtn"]')


button_after = wait.until(
    EC.invisibility_of_element_located(NO_VISIBLE_TEXT) and
    EC.element_to_be_clickable(BUTTON_TEXT)
)
button_after.click()

alert = driver.switch_to.alert
alert.accept()


wait.until(
    EC.text_to_be_present_in_element(INVVIB_TEXT, "This text is displayed after 10 seconds of wait.")
)
print("Текст появился")

eneblet_buton=wait.until(EC.element_to_be_clickable(ENEBLET),"Элемент не активен")
eneblet_buton.click()

print("тест прошел_1")

alert = driver.switch_to.alert
alert.accept()

deseble_buton= driver.find_element(*DESEBLET).is_enabled()
eneblet_buton.click()

print(F"тест прошел_2{deseble_buton}")



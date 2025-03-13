import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--window-size=1920,1080")


driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://chat.deepseek.com/")
time.sleep(2)

a = driver.get_cookies() # Получение всех куки они словарём в списке
print(*a,sep='\n')
print("___________________")
print(driver.get_cookie("HWWAFSESID")) # Получение куки по name

driver.add_cookie({
    'name': 'Example',
    'value': 'Kukushka'
}) # Добавление куке

driver.delete_cookie() # Удаление одного куки
driver.delete_all_cookies() # Удаление всех куков
from selenium import webdriver

# Поменял запись!!! Тестирую команду git revert

driver = webdriver.Chrome()

driver.get("https://chat.deepseek.com/")

"""
2. Инициализация через WebDriverManager

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

2. Инициализация через WebDriverManager + версия Chrome

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager(driver_version="114.0.5735.16").install())
driver = webdriver.Chrome(service=service)
"""

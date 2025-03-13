import os
import time

from selenium import webdriver


"""
➖ Скачивание: https://the-internet.herokuapp.com/download
➖ Загрузка: https://the-internet.herokuapp.com/upload
"""
chrome_options = webdriver.ChromeOptions()
# Скачивание файла
# os.getcwd() возвращает место где находится код
prefs = {
    "download.default_directory": f"{os.getcwd()}\\downloads"
}      # специфические настройки браузера
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options)
driver.get("https://the-internet.herokuapp.com/download")

driver.find_elements("xpath", '//*[@id="content"]/div/a')[3].click()

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

driver.get('https://the-internet.herokuapp.com/upload')

driver.find_element('xpath', '//*[@id="file-upload"]').send_keys(f"{os.getcwd()}\\downloads\\0a84337f-beb9-4f3b-84d2-b011da6f4121.tmp")
time.sleep(2)
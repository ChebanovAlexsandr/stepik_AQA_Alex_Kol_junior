from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://ru.wikipedia.org")

url = driver.current_url        # Провека что открылась нужная URL
print("URL странице", url)

current_title = driver.title
print("Тайтл страници", current_title)

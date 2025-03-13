import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")

full_name = driver.find_element("xpath", '//input[@placeholder="Full Name"]')
email = driver.find_element("xpath", '//input[@placeholder="name@example.com"]')
current_address = driver.find_elements("xpath", '//*[@id="currentAddress"]')[0]
permanent_address = driver.find_elements("xpath", '//*[@id="permanentAddress"]')[0]
submit = driver.find_element("xpath", '//*[@id="submit"]')

full_name_txt = driver.find_element("xpath", '//*[@id="name"]/text()[2]')
email_txt = driver.find_element("xpath", '//*[@id="email"]/text()[2]')
current_address_txt = driver.find_element("xpath", '//*[@id="currentAddress"]/text()[2]"]')
permanent_address_txt = driver.find_element("xpath", '//*[@id="permanentAddress"]/text()[2]')

empty_full_name = full_name.get_attribute("value")
full_name.send_keys("Alex")
fill_full_name = full_name.get_attribute("value")
assert empty_full_name != fill_full_name, 'Поле не заполнено'

empty_email = email.get_attribute("value")
email.send_keys("alex@mail.ru")
fill_email = email.get_attribute("value")
assert empty_email != fill_email, 'Поле не заполнено'

empty_current_address = current_address.get_attribute("value")
current_address.send_keys("Los Angelec")
fill_current_address = current_address.get_attribute("value")
assert empty_current_address != fill_current_address, 'Поле не заполнено'

empty_permanent_address = permanent_address.get_attribute("value")
permanent_address.send_keys("Puskin_1_kB_13")
fill_permanent_address = permanent_address.get_attribute("value")
assert empty_permanent_address != fill_permanent_address, 'Поле не заполнено'

submit.click()





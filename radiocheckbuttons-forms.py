from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://thegoldbugs.com/")

fieldset = driver.find_element(By.ID, 'checkbox-b5b9cc19-24e5-4c8c-960a-055837723942')
print(fieldset.tag_name)

checkboxes = fieldset.find_elements(By.XPATH, '//input[@type="checkbox"]')
checkbox1 = checkboxes[1]

print(checkbox1.get_attribute('value'))
print(checkbox1.is_selected())

checkbox1.click()
print(checkbox1.is_selected())

radio_buttons = fieldset.find_elements(By.XPATH, '//input[@type="radio"]')
print(len(radio_buttons))
radio_button1 = radio_buttons[5]
print(radio_button1.get_attribute('value'))

print(radio_button1.is_selected())
radio_button1.click()
print(radio_button1.is_selected())

driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://python.org/")

input_element = driver.find_element(By.NAME, 'q')
print(input_element.tag_name)

input_element.get_attribute('placeholder')
print(input_element.text)

SEARCH_TEXT = 'python news'
input_element.send_keys(SEARCH_TEXT)

input_element.clear()

search_button = driver.find_element(By.ID, 'submit')
print(search_button.text)

input_element.send_keys(SEARCH_TEXT)
search_button.click()
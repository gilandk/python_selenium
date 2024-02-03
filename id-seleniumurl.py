
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.selenium.dev/")

element1 = driver.find_element(By.ID, 'Layer_1')

print(element1.tag_name)

element1.get_attribute('data-name')

element2 = driver.find_element(By.CSS_SELECTOR, 'svg#Layer_1')

print(element2.get_attribute('data-name'))

driver.quit()
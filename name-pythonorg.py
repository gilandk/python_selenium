
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.python.org/")

element1 = driver.find_element(By.NAME, 'q')
print(element1.tag_name)
print(element1.get_attribute('class'))

element2 = driver.find_element(By.NAME, 'submit')
print(element2.text)
print(element2.get_attribute('value'))

element3 = driver.find_element(By.NAME, 'keywords')
print(element3.text)
print(element3.get_attribute('content'))
print(element3.get_attribute('content').split())

driver.quit()
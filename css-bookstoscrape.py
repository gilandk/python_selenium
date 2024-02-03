from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://books.toscrape.com/")

element1 = driver.find_element(By.CSS_SELECTOR, 'div.alert.alert-warning')

print(element1.text)

element2 = driver.find_element(By.CSS_SELECTOR, 'ul.nav.nav-list')

print(element2.text)

element3 = driver.find_element(By.CSS_SELECTOR, 'div#messages')

print(element3.text)

img_elements = driver.find_elements(By.CSS_SELECTOR, 'img')

for element in img_elements:
    print(element.get_attribute('alt'))
    
driver.quit()
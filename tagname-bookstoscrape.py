from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://books.toscrape.com/")


img_elements = driver.find_elements(By.TAG_NAME, 'img')

for element in img_elements[0:10]:
    print(element.get_attribute('alt'))

link_elements = driver.find_elements(By.TAG_NAME, 'a')
for link in link_elements[0:10]:
    print(link.get_attribute('title') or link.text)
    print(link.get_attribute('href'))

driver.quit()
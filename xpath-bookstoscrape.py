from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://books.toscrape.com/")


link_elements = driver.find_elements(By.XPATH, '//a[@title]')
print(len(link_elements))
print(link_elements[0].get_attribute('title'))

price_element = driver.find_element(By.XPATH, '//a[@title = "A Light in the Attic"]/../../div[@class="product_price"]/p[@class="price_color"]')
print(price_element.text)

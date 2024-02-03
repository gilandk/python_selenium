from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://books.toscrape.com/")

book_element = driver.find_element(By.CSS_SELECTOR, 'article.product_pod')
print(book_element.text)
print(book_element.tag_name)
print(book_element.size)
print(book_element.is_displayed())
print(book_element.is_enabled())
print(book_element.is_selected())

book_element.screenshot('test.png')

button_element = book_element.find_element(By.CSS_SELECTOR, 'button')
print(button_element.text)
print(button_element.get_dom_attribute('type'))
print(button_element.get_attribute('type'))
print(button_element.get_property('name'))
print(button_element.value_of_css_property('color'))

print(button_element.value_of_css_property('padding'))

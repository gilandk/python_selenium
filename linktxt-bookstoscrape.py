from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://books.toscrape.com/")


link_elements = driver.find_element(By.LINK_TEXT, 'Tipping the Velvet')
print(link_elements.text)
print(link_elements.tag_name)

add_elements = driver.find_elements(By.PARTIAL_LINK_TEXT, 'Sh')
print([elem.text for elem in add_elements])

driver.quit()

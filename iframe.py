from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://jqueryui.com/" + 'draggable')

iframe_element = driver.find_element(By.CSS_SELECTOR, 'iframe.demo-frame')
driver.switch_to.frame(iframe_element)

draggable_element = driver.find_element(By.ID, 'draggable')

print(draggable_element.tag_name)

driver.switch_to.default_content()

main_nav = driver.find_element(By.ID, 'main')
print(main_nav.tag_name)

driver.quit()

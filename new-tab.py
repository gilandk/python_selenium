from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://books.toscrape.com/")
driver.switch_to.new_window('tab')

driver.get("https://python.org/")



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://books.toscrape.com/")
driver.get("https://python.org/")
driver.get("https://quotes.toscrape.com/")

driver.back()
driver.back()
driver.forward()

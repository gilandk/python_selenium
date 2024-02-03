from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

B = "https://books.toscrape.com/"

driver.get(B)

size = driver.get_window_size()
print(size)

print(driver.get_window_position())

rect = driver.get_window_rect()
print(rect)

driver.minimize_window()
driver.maximize_window()
driver.set_window_rect(x=20, y=50, height = 600, width=600)
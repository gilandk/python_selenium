from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)


driver.get("https://books.toscrape.com/")
js = 'alert("Hey! This is an alert!")'
driver.execute_script(js)

alert = driver.switch_to.alert
print(alert.text)

alert.accept()
opt = 'confirm("Do you want to confirm?")'
print(driver.execute_script(opt))
print(alert.text)

alert.dismiss()

driver.quit()
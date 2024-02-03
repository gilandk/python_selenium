from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

P = "https://python.org"
B = "https://books.toscrape.com/"

driver.get(P)

print(driver.get_cookies())

print(driver.add_cookie({
    'name': 'cookie1',
    'value': 'Look at me!'
}))

loc_storage = "window.localStorage.setItem('key1','value1')"
driver.execute_script(loc_storage)

ret_loc_storage = "return window.localStorage.getItem('key1')"
print(driver.execute_script(ret_loc_storage))

sess_storage = "window.sessionStorage.setItem('key8','value8')"
driver.execute_script(sess_storage)

ret_sess_storage = "window.sessionStorage.getItem('key8')"
print(driver.execute_script(ret_sess_storage))

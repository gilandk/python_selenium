from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://books.toscrape.com/")

buttons = driver.find_elements(By.TAG_NAME, 'button')

button1 = buttons[0]

print(button1.text)

button1.click()

buttons = driver.find_elements(By.TAG_NAME, 'button')

button1 = buttons[0]

print(button1.text)

actions = ActionChains(driver)

actions.context_click(on_element=button1).perform()

actions.click_and_hold(on_element=button1).perform()

actions.release().perform()

link_element = driver.find_element(By.TAG_NAME, 'a')

print(link_element.text)

link_element.click()

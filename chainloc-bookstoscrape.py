from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(options=options)
driver.get("https://books.toscrape.com/")

book_elements = driver.find_elements(By.CSS_SELECTOR, 'article.product_pod')
print(len(book_elements))

print(book_elements[0].find_element(By.TAG_NAME, 
                                    'img').get_attribute('alt'))

print(book_elements[0].find_element(By.CSS_SELECTOR, 
                                    'p.price_color').text)


price_list = []

for book in book_elements:
    price_list.append({
        'title': book.find_element(By.TAG_NAME, 'img').get_attribute('alt'),
        'price': book.find_element(By.CSS_SELECTOR, 'p.price_color').text
    })
    
print(price_list)

driver.quit()

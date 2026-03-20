from time import sleep
from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

o=EdgeOptions()
o.add_experimental_option("detach", True)
driver = Edge(options=o)
driver.get("https://www.saucedemo.com/")

driver.maximize_window()
sleep(2)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='user-name']"))).send_keys("standard_user")
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='password']"))).send_keys("secret_sauce")
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='login-button']"))).click()
sleep(2)
title=wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='title']")))
print(title.text)
product = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))
print("Product Names:")
for i in product:
    print(i.text)
price = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_price")))
print("Product Prices:")
for i  in price:
    print(i.text)

buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[text()='Add to cart']")))
buttons[3].click()
print("4th product added to cart successfully!")
driver.quit()

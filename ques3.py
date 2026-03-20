from time import sleep
from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

o=EdgeOptions()
o.add_experimental_option("detach", True)
driver = Edge(options=o)
driver.get("https://www.shine.com/registration/")

driver.maximize_window()
sleep(2)
driver.implicitly_wait(10)
driver.find_element(By.ID,"id_file").send_keys(r'C:\Users\Pratibha\OneDrive\Documents\Andree Rocher.docx')
sleep(4)
driver.quit()
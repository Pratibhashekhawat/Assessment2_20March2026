from time import sleep
from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By

o=EdgeOptions()
o.add_experimental_option("detach", True)
driver = Edge(options=o)
driver.get("https://www.prokabaddi.com/")

driver.maximize_window()
sleep(2)
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//span[text()='Standings']").click()
matches=driver.find_element(By.XPATH,"(//p[@class='count'])[36]")
won=driver.find_element(By.XPATH,"(//p[@class='count'])[37]")
lost=driver.find_element(By.XPATH,"(//p[@class='count'])[38]")
sd=driver.find_element(By.XPATH,"(//p[@class='count'])[39]")
points=driver.find_element(By.XPATH,"(//p[@class='count'])[40]")
print("matches:"+matches.text)
print("won:"+won.text)
print("lost:"+lost.text)
print("score difference:"+sd.text)
print("points:"+points.text)
driver.quit()


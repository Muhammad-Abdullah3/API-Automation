import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import pyautogui as pg
import time
print("Hello")
driver = uc.Chrome()
print("Hello")
driver.get("https://www.youtube.com/")
home = driver.find_element(By.XPATH,'//a[@title="YouTube Home"]')
loc = home.location
print(loc)
x = loc['x']
y = loc['y']
print(x,"    ", y)
time.sleep(10)
pg.click(x,y,duration=3)
time.sleep(100)
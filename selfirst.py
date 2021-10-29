from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

file = input("enter a video name =")

PATH = "D:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.youtube.com")
def search(name):
    my_vid = driver.find_element_by_id("search")
    my_vid.send_keys(name)
    my_vid.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.find_element_by_id("video-title").click()


search(file)







'''
mail = driver.find_element_by_id("email")
mail.send_keys("swastik_aryal@hotmail.com")
myp = driver.find_element_by_id("pass")
myp.send_keys("hahahuhu654321")
myp.send_keys(Keys.RETURN)
time.sleep(10)


try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_1mf _1mj"))
    )
    element.send_keys("k cha")
except:
    driver.quit()
'''

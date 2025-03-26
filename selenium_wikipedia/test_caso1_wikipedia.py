from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service("/opt/homebrew/bin/chromedriver")  
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

# Caso 1: Prueba de búsqueda en Wikipedia
driver.get("https://www.wikipedia.org/")
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Brasil")
search_box.send_keys(Keys.RETURN)
time.sleep(3)
assert "Brasil" in driver.title 
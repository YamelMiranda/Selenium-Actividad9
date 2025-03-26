from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service("/opt/homebrew/bin/chromedriver")  
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

# Caso 2: Cambio de idioma a Español
driver.get("https://www.wikipedia.org/")
driver.find_element(By.LINK_TEXT, "Español").click()
time.sleep(5)
assert "Wikipedia, la enciclopedia libre" in driver.title  
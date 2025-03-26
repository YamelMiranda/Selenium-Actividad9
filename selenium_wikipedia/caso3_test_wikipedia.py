from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service("/opt/homebrew/bin/chromedriver")  
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

# Caso 3: Navegación a un artículo desde la página principal
driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")
driver.find_element(By.CSS_SELECTOR, "a[title='Portal:Actualidad']").click()
time.sleep(4)
assert "Portal:Actualidad" in driver.title  
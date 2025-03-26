from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("/opt/homebrew/bin/chromedriver")  
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

# Caso 4: Verificación del enlace de donaciones con esperas explícitas
wait = WebDriverWait(driver, 10)
donate_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Donate")))
donate_link.click()

assert "donate" in driver.current_url  

driver.quit()

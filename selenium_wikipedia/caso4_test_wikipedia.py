from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

service = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)



service = Service("/opt/homebrew/bin/chromedriver")  
driver = webdriver.Chrome(service=service)


driver.get("https://www.wikipedia.org/")

try:
   
    donate_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Donate"))
    )
    donate_link.click()

    
    WebDriverWait(driver, 5).until(
        EC.url_contains("donate")
    )
    assert "donate" in driver.current_url  
    print("✅ Prueba exitosa: Se accedió a la página de donaciones.")

except Exception as e:
    print(f"❌ Error en la prueba: {e}")

finally:
    driver.quit()

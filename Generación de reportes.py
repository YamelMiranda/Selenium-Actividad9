import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def driver():
    service = Service("/opt/homebrew/bin/chromedriver")  
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.wikipedia.org/")
    yield driver
    driver.quit()

def test_title(driver):
    """Verifica que 'Wikipedia' esté en el título"""
    assert "Wikipedia" in driver.title

def test_donate_link(driver):
    """Verifica que el enlace de donaciones funciona"""
    donate_link = driver.find_element(By.LINK_TEXT, "Donate")
    donate_link.click()
    assert "donate" in driver.current_url

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def driver():

    firefox_options = Options()
    firefox_options.add_argument("--start-maximized") 
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")
    firefox_options.add_argument("--disable-extensions")  
    
    service = Service(r"C:\webdrivers\geckodriver.exe")
    driver = webdriver.Firefox(
        service=service,
        options=firefox_options
    )


    yield driver 
    
    driver.quit()
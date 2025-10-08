import allure
import sys
import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from locators.main_page_locators import MainPageLocators



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        self.find_element(locator).click()

    def send_keys_to_input(self, locator, keys):
        self.find_element(locator).send_keys(keys)
        
    def send_keys(self, element, keys):
        element.send_keys(keys)

    def wait_element_to_be_cliackable_and_click(self, locator):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        element.click()

    def scroll_to_element_and_click(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def check_new_window_url(self, url):
        WebDriverWait(self.driver, 5).until(
            lambda driver: len(driver.window_handles) > 1
        )
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        WebDriverWait(self.driver, 5).until(
            EC.url_contains(url)
        )
        current_url = self.driver.current_url
        assert url in current_url
import allure
import sys
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from locators.main_page_locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('Нажимаем на кнопку заказать в header')
    def click_order_header_button(self):
        self.driver.find_element(*MainPageLocators.order_header_button).click()

    @allure.step('Нажимаем на кнопку заказать на главной странице')
    def click_order_button(self):
        element = self.driver.find_element(*MainPageLocators.order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
    @allure.step('Нажимаем на логотип яндекс')
    def click_yandex_logo_button(self):
        self.driver.find_element(*MainPageLocators.yandex_logo_button).click()
    @allure.step('Проверяем, что перешли в dzen')
    def check_dzen_redirect(self):
        WebDriverWait(self.driver, 5).until(
            lambda driver: len(driver.window_handles) > 1
        )
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        WebDriverWait(self.driver, 5).until(
            EC.url_contains("dzen.ru")
        )
        current_url = self.driver.current_url
        assert "dzen.ru" in current_url
    @allure.step('Кликаем и проверяем, что перешли на главную страницу')
    def click_and_check_dzen_redirect(self):
        self.click_yandex_logo_button()
        self.check_dzen_redirect()

    @allure.step('Нажимаем на Самокат в header')
    def click_scooter_logo_button(self):
        self.driver.find_element(*MainPageLocators.scooter_logo_button).click()
    @allure.step('Проверяем, что перешли на главную страницу')
    def check_main_page_redirect(self):
        assert self.driver.find_element(*MainPageLocators.main_page_text)
    @allure.step('Кликаем и проверяем, что перешли на главную страницу')
    def click_and_check_main_page_redirect(self):
        self.click_scooter_logo_button()
        self.check_main_page_redirect()


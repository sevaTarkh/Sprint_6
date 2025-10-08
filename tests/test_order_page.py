import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import allure
from data.data import Constants
from pages.order_page import OrderPage
from pages.main_page import MainPage

class TestOrderPage:

    @allure.title('Заказ самоката через header')
    @allure.description('На странице ищем элемент заказать в header и заказываем самокат. Переходим на главную страницу. Переходим в dzen')
    def test_order_scooter_from_header(self, driver):
        driver.get(Constants.url_samokat)
        order_page = OrderPage(driver)
        main_page = MainPage(driver)

        main_page.click_order_header_button()
        order_page.order_scooter()

        main_page.click_and_check_main_page_redirect()
        main_page.click_and_check_dzen_redirect()

    @allure.title('Заказ самоката через кнопку на главной странице')
    @allure.description('На странице ищем элемент заказать и заказываем самокат. Переходим на главную страницу. Переходим в dzen')
    def test_order_scooter(self, driver):
        driver.get(Constants.url_samokat)
        order_page = OrderPage(driver)
        main_page = MainPage(driver)

        main_page.click_order_button()
        order_page.order_scooter(name='Ярослав', last_name='Петров', address='Москва 13', phone='098765432100', subway='Б', date='02', comment='ббббббб', one_day=False)

        main_page.click_and_check_main_page_redirect()
        main_page.click_and_check_dzen_redirect()
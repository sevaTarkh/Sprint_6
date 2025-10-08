import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import allure
from selenium.webdriver.common.keys import Keys
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step('Заполнения поля "Имя"')
    def send_keys_name_input(self, name='Всеволод'):
        self.send_keys_to_input(OrderPageLocators.name_input, name)

    @allure.step('Заполнения поля "Фамилия"')
    def send_keys_last_name_input(self, last_name='Тарханов'):
        self.send_keys_to_input(OrderPageLocators.last_name_input, last_name)
    
    @allure.step('Заполнения поля "Адрес"')
    def send_keys_address_input(self, address='Вот такой вот адрес'):
        self.send_keys_to_input(OrderPageLocators.address_input, address)
    

    @allure.step('Заполнения поля "Телефон"')
    def send_keys_phone_input(self, phone='12345678901'):
        self.send_keys_to_input(OrderPageLocators.number_input, phone)

    @allure.step('Заполнения поля "Метро"')
    def send_keys_subway_input(self, subway='Ака'):
        element = self.find_element(OrderPageLocators.subway_input)
        self.send_keys(element, subway)
        self.send_keys(element, Keys.ARROW_DOWN)
        self.send_keys(element, Keys.ENTER)

    @allure.step('Заполнения форму для кого самокат')
    def fill_out_the_form_for_whom_the_scooter_is(self, name='Всеволод', last_name='Тарханов', address='Вот такой вот адрес', phone='12345678901', subway='Ака'):
        self.send_keys_name_input(name)
        self.send_keys_last_name_input(last_name)
        self.send_keys_address_input(address)
        self.send_keys_phone_input(phone)
        self.send_keys_subway_input(subway)

    @allure.step('Нажимаем на кнопку далее')
    def click_next_button(self):
        self.wait_element_to_be_cliackable_and_click(OrderPageLocators.next_button)

    @allure.step('Заполнения поля "Дата"')
    def send_keys_date_input(self, date='01'):
        element = self.find_element(OrderPageLocators.date_input)
        self.send_keys(element, date)
        self.send_keys(element, Keys.ENTER)

    @allure.step('Заполнения поля "Комментарий"')
    def send_keys_comment_input(self, comment='живу в подвале'):
        self.send_keys_to_input(OrderPageLocators.comment_input, comment)

    @allure.step('Заполнения поля "Цвет черный"')
    def click_color_black_input(self):
        self.click_element(OrderPageLocators.color_black_input)
    
    @allure.step('Заполнения поля "Цвет серый"')
    def click_color_grey_input(self):
        self.click_element(OrderPageLocators.color_grey_input)

    @allure.step('Заполнения поля "срок"')
    def choose_period_input(self, one_day=True):
        self.click_element(OrderPageLocators.rental_period_input)
        if one_day:
            self.click_element(OrderPageLocators.one_day)
        else:
            self.click_element(OrderPageLocators.two_days)
            
    @allure.step('Заполнения форму про аренду')
    def fill_out_the_form_about_rent(self, date='01', comment='аааааааааа', one_day=True):
        self.send_keys_date_input(date)
        self.send_keys_comment_input(comment)
        self.choose_period_input(one_day)
        self.click_color_black_input()
        self.click_color_grey_input()

    @allure.step('Заказываем самокат')
    def click_order_button(self):
        self.click_element(OrderPageLocators.final_order_button)

    @allure.step('Подтвержаем что хотим самокат')
    def click_yes_button(self):
        self.click_element(OrderPageLocators.yes_button)

    @allure.step('Проверка что заказ оформлен')
    def checking_the_order_has_been_placed(self):
        assert self.find_element(OrderPageLocators.order_done)


    @allure.step('Нажимаем на кнопку Посмотреть статус')
    def click_watch_button(self):
        self.click_element(OrderPageLocators.watch_status)

    @allure.step('Заказываем самокат')
    def order_scooter(self, name='Всеволод', last_name='Тарханов', address='Вот такой вот адрес', phone='12345678901', subway='Ака', date='01', comment='аааааааааа', one_day=True):
        self.fill_out_the_form_for_whom_the_scooter_is(name, last_name, address, phone, subway)
        self.click_next_button()

        self.fill_out_the_form_about_rent(date, comment, one_day)
        self.click_order_button()
        self.click_yes_button()

        self.checking_the_order_has_been_placed()

        self.click_watch_button()
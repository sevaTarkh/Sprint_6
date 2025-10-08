import allure
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step('Нажимаем на кнопку заказать в header')
    def click_order_header_button(self):
        self.click_element(MainPageLocators.order_header_button)

    @allure.step('Нажимаем на кнопку заказать на главной странице')
    def click_order_button(self):
        self.scroll_to_element_and_click(MainPageLocators.order_button)

    @allure.step('Нажимаем на логотип яндекс')
    def click_yandex_logo_button(self):
        self.click_element(MainPageLocators.yandex_logo_button)

    @allure.step('Проверяем, что перешли в dzen')
    def check_dzen_redirect(self):
        self.check_new_window_url("dzen.ru")

    @allure.step('Кликаем и проверяем, что перешли на главную страницу')
    def click_and_check_dzen_redirect(self):
        self.click_yandex_logo_button()
        self.check_dzen_redirect()

    @allure.step('Нажимаем на Самокат в header')
    def click_scooter_logo_button(self):
        self.click_element(MainPageLocators.scooter_logo_button)

    @allure.step('Проверяем, что перешли на главную страницу')
    def check_main_page_redirect(self):
        assert self.find_element(MainPageLocators.main_page_text)

    @allure.step('Кликаем и проверяем, что перешли на главную страницу')
    def click_and_check_main_page_redirect(self):
        self.click_scooter_logo_button()
        self.check_main_page_redirect()


    @allure.step('Нажимаем на вопрос "Сколько это стоит? И как оплатить?"')
    def click_how_much_does_it_cost_button(self):
        self.scroll_to_element_and_click(MainPageLocators.how_much_does_it_cost_button)

    @allure.step('Проверяем ответ на вопрпос "Сколько это стоит? И как оплатить?"')    
    def check_correct_answer_how_much(self):
        self.click_how_much_does_it_cost_button()
        assert self.find_element(MainPageLocators.how_much_does_it_cost_answer)


    @allure.step('Нажимаем на вопрос "Хочу сразу несколько самокатов! Так можно?"')
    def click_want_several_scooters_button(self):
        self.scroll_to_element_and_click(MainPageLocators.want_several_scooters_button)

    @allure.step('Проверяем ответ на вопрос "Хочу сразу несколько самокатов! Так можно?"')
    def check_correct_answer_want_several_scooters(self):
        self.click_want_several_scooters_button()
        assert self.find_element(MainPageLocators.want_several_scooters_answer)


    @allure.step('Нажимаем на вопрос "Как рассчитывается время аренды?"')
    def click_what_time_rent_button(self):
        self.scroll_to_element_and_click(MainPageLocators.what_time_rent_button)

    @allure.step('Проверяем ответ на вопрос "Как рассчитывается время аренды?"')
    def check_correct_answer_what_time_rent(self):
        self.click_what_time_rent_button()
        assert self.find_element(MainPageLocators.what_time_rent_answer)


    @allure.step('Нажимаем на вопрос "Можно ли заказать самокат прямо на сегодня?"')
    def click_can_i_order_scooter_now_button(self):
        self.scroll_to_element_and_click(MainPageLocators.can_i_order_scooter_now_button)

    @allure.step('Проверяем ответ на вопрос "Можно ли заказать самокат прямо на сегодня?"')
    def check_correct_answer_can_i_order(self):
        self.click_can_i_order_scooter_now_button()
        assert self.find_element(MainPageLocators.can_i_order_scooter_now_answer)


    @allure.step('Нажимаем на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    def click_can_i_return_scooter_earlier_button(self):
        self.scroll_to_element_and_click(MainPageLocators.can_i_return_scooter_earlier_button)

    @allure.step('Проверяем ответ на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    def check_correct_answer_can_i_return(self):
        self.click_can_i_return_scooter_earlier_button()
        assert self.find_element(MainPageLocators.can_i_return_scooter_earlier_answer)


    @allure.step('Нажимаем на вопрос "Вы привозите зарядку вместе с самокатом?"')
    def click_do_u_bring_charger_button(self):
        self.scroll_to_element_and_click(MainPageLocators.do_u_bring_charger_button)

    @allure.step('Проверяем ответ на вопрос "Вы привозите зарядку вместе с самокатом?"')
    def check_correct_answer_do_u_bring(self):
        self.click_do_u_bring_charger_button()
        assert self.find_element(MainPageLocators.do_u_bring_charger_answer)


    @allure.step('Нажимаем на вопрос "Можно ли отменить заказ?"')
    def click_can_i_cancel_order_button(self):
        self.scroll_to_element_and_click(MainPageLocators.can_i_cancel_order_button)

    @allure.step('Проверяем ответ на вопрос "Можно ли отменить заказ?"')
    def check_correct_answer_can_i_cancel(self):
        self.click_can_i_cancel_order_button()
        assert self.find_element(MainPageLocators.can_i_cancel_order_answer)


    @allure.step('Нажимаем на вопрос "Я живу за МКАДом, привезёте?"')
    def click_i_from_mkad_button(self):
        self.scroll_to_element_and_click(MainPageLocators.i_from_mkad_button)

    @allure.step('Проверяем ответ на вопрос "Я живу за МКАДом, привезёте?"')
    def check_correct_answer_i_from_mkad(self):
        self.click_i_from_mkad_button()
        assert self.find_element(MainPageLocators.i_from_mkad_answer)

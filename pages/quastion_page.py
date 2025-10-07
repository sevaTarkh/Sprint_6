import allure
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from locators.quastion_page_locators import QuastionPageLocators


class QuastionPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем на вопрос "Сколько это стоит? И как оплатить?"')
    def click_how_much_does_it_cost_button(self):
        element = self.driver.find_element(*QuastionPageLocators.how_much_does_it_cost_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
    @allure.step('Проверяем ответ на вопрпос "Сколько это стоит? И как оплатить?"')    
    def check_correct_answer_how_much(self):
        self.click_how_much_does_it_cost_button()
        assert self.driver.find_element(*QuastionPageLocators.how_much_does_it_cost_answer)


    @allure.step('Нажимаем на вопрос "Хочу сразу несколько самокатов! Так можно?"')
    def click_want_several_scooters_button(self):
        element = self.driver.find_element(*QuastionPageLocators.want_several_scooters_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
    @allure.step('Проверяем ответ на вопрос "Хочу сразу несколько самокатов! Так можно?"')
    def check_correct_answer_want_several_scooters(self):
        self.click_want_several_scooters_button()
        assert self.driver.find_element(*QuastionPageLocators.want_several_scooters_answer)


    @allure.step('Нажимаем на вопрос "Как рассчитывается время аренды?"')
    def click_what_time_rent_button(self):
        element = self.driver.find_element(*QuastionPageLocators.what_time_rent_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
    @allure.step('Проверяем ответ на вопрос "Как рассчитывается время аренды?"')
    def check_correct_answer_what_time_rent(self):
        self.click_what_time_rent_button()
        assert self.driver.find_element(*QuastionPageLocators.what_time_rent_answer)


    @allure.step('Нажимаем на вопрос "Можно ли заказать самокат прямо на сегодня?"')
    def click_can_i_order_scooter_now_button(self):
        element = self.driver.find_element(*QuastionPageLocators.can_i_order_scooter_now_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
    @allure.step('Проверяем ответ на вопрос "Можно ли заказать самокат прямо на сегодня?"')
    def check_correct_answer_can_i_order(self):
        self.click_can_i_order_scooter_now_button()
        assert self.driver.find_element(*QuastionPageLocators.can_i_order_scooter_now_answer)


    @allure.step('Нажимаем на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    def click_can_i_return_scooter_earlier_button(self):
        element = self.driver.find_element(*QuastionPageLocators.can_i_return_scooter_earlier_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
    @allure.step('Проверяем ответ на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    def check_correct_answer_can_i_return(self):
        self.click_can_i_return_scooter_earlier_button()
        assert self.driver.find_element(*QuastionPageLocators.can_i_return_scooter_earlier_answer)


    @allure.step('Нажимаем на вопрос "Вы привозите зарядку вместе с самокатом?"')
    def click_do_u_bring_charger_button(self):
        element = self.driver.find_element(*QuastionPageLocators.do_u_bring_charger_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
    @allure.step('Проверяем ответ на вопрос "Вы привозите зарядку вместе с самокатом?"')
    def check_correct_answer_do_u_bring(self):
        self.click_do_u_bring_charger_button()
        assert self.driver.find_element(*QuastionPageLocators.do_u_bring_charger_answer)


    @allure.step('Нажимаем на вопрос "Можно ли отменить заказ?"')
    def click_can_i_cancel_order_button(self):
        element = self.driver.find_element(*QuastionPageLocators.can_i_cancel_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
    @allure.step('Проверяем ответ на вопрос "Можно ли отменить заказ?"')
    def check_correct_answer_can_i_cancel(self):
        self.click_can_i_cancel_order_button()
        assert self.driver.find_element(*QuastionPageLocators.can_i_cancel_order_answer)


    @allure.step('Нажимаем на вопрос "Я жизу за МКАДом, привезёте?"')
    def click_i_from_mkad_button(self):
        element = self.driver.find_element(*QuastionPageLocators.i_from_mkad_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
    @allure.step('Проверяем ответ на вопрос "Я жизу за МКАДом, привезёте?"')
    def check_correct_answer_i_from_mkad(self):
        self.click_i_from_mkad_button()
        assert self.driver.find_element(*QuastionPageLocators.i_from_mkad_answer)
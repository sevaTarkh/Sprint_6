import sys
import pytest
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import allure
from pages.quastion_page import QuastionPage
from data.data import Constants


class TestQuastionPage:

    @allure.title('Проверка ответов на вопросы')
    @allure.description('На странице ищем элемент вопрос, нажимаем на него и проверяем корректный ответ')
    @pytest.mark.parametrize("test_method", [
        "check_correct_answer_how_much",
        "check_correct_answer_want_several_scooters", 
        "check_correct_answer_what_time_rent",
        "check_correct_answer_can_i_order",
        "check_correct_answer_can_i_return",
        "check_correct_answer_do_u_bring",
        "check_correct_answer_can_i_cancel",
        "check_correct_answer_i_from_mkad"
    ])
    def test_check_answers(self, driver, test_method):
        driver.get(Constants.url_samokat)
        quastion_page = QuastionPage(driver)
        
        # Получаем метод по имени и вызываем его
        method = getattr(quastion_page, test_method)
        method()
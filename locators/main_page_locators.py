from selenium.webdriver.common.by import By
from data.data import Constants

class MainPageLocators:
    order_header_button = [By.XPATH, "(//button[text()='Заказать'])[1]"]
    order_button = [By.XPATH, "(//button[text()='Заказать'])[2]"]
    yandex_logo_button = [By.XPATH, "//img[@alt='Yandex']"]
    scooter_logo_button = [By.XPATH, "//img[@alt='Scooter']"]
    
    main_page_text = [By.XPATH, "//div[contains(text(), 'Самокат')]"]

    how_much_does_it_cost_button = [By.XPATH, "//div[text()='Сколько это стоит? И как оплатить?']"]
    how_much_does_it_cost_answer = [By.XPATH, f"//p[text()='{Constants.how_much_does_it_cost_answer}']"]

    want_several_scooters_button = [By.XPATH, "//div[text()='Хочу сразу несколько самокатов! Так можно?']"]
    want_several_scooters_answer = [By.XPATH, f"//p[text()='{Constants.want_several_scooters_answer}']"]

    what_time_rent_button = [By.XPATH, "//div[text()='Как рассчитывается время аренды?']"]
    what_time_rent_answer = [By.XPATH, f"//p[text()='{Constants.what_time_rent_answer}']"]

    can_i_order_scooter_now_button = [By.XPATH, "//div[text()='Можно ли заказать самокат прямо на сегодня?']"]
    can_i_order_scooter_now_answer = [By.XPATH, f"//p[text()='{Constants.can_i_order_scooter_now_answer}']"]

    can_i_return_scooter_earlier_button = [By.XPATH, "//div[text()='Можно ли продлить заказ или вернуть самокат раньше?']"]
    can_i_return_scooter_earlier_answer = [By.XPATH, f"//p[text()='{Constants.can_i_return_scooter_earlier_answer}']"]

    do_u_bring_charger_button = [By.XPATH, "//div[text()='Вы привозите зарядку вместе с самокатом?']"]
    do_u_bring_charger_answer = [By.XPATH, f"//p[text()='{Constants.do_u_bring_charger}']"]

    can_i_cancel_order_button = [By.XPATH, "//div[text()='Можно ли отменить заказ?']"]
    can_i_cancel_order_answer = [By.XPATH, f"//p[text()='{Constants.can_i_cancel_order_answer}']"]

    i_from_mkad_button =[By.XPATH, "//div[text()='Я жизу за МКАДом, привезёте?']"]
    i_from_mkad_answer = [By.XPATH, f"//p[text()='{Constants.i_from_mkad_answer_answer}']"]

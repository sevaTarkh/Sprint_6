from selenium.webdriver.common.by import By


class OrderPageLocators:
    name_input = [By.XPATH, "//input[@placeholder='* Имя']"]
    last_name_input = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    address_input = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    number_input = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    subway_input = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    next_button = [By.XPATH, "//button[text()='Далее']"]

    date_input = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    rental_period_input = [By.XPATH, "//div[text()='* Срок аренды']"]
    one_day = [By.XPATH, "//div[text()='сутки']"]
    two_days = [By.XPATH, "//div[text()='двое суток']"]
    color_black_input = [By.ID, "black"]
    color_grey_input = [By.ID, "grey"]
    comment_input = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]

    final_order_button = [By.XPATH, "(//button[text()='Заказать'])[2]"]
    yes_button = [By.XPATH, "//button[text()='Да']"]
    
    order_done = [By.XPATH, "//div[contains(text(),'Заказ оформлен')]"]
    watch_status = [By.XPATH, "//button[text()='Посмотреть статус']"]


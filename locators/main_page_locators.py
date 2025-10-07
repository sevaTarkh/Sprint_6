from selenium.webdriver.common.by import By

class MainPageLocators:
    order_header_button = [By.XPATH, "(//button[text()='Заказать'])[1]"]
    order_button = [By.XPATH, "(//button[text()='Заказать'])[2]"]
    yandex_logo_button = [By.XPATH, "//img[@alt='Yandex']"]
    scooter_logo_button = [By.XPATH, "//img[@alt='Scooter']"]
    
    main_page_text = [By.XPATH, "//div[contains(text(), 'Самокат')]"]

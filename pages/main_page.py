import time

from pages.locators import MainPageLocators, OrderADebtCardLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class MainPage(BasePage):
    def go_to_login_page(self):
        login_button = self.browser.find_element(*MainPageLocators.LOGIN_BUTTON)
        login_button.click()
        login_page_link = self.browser.current_url
        assert login_page_link == 'https://online.gpb.ru/login', 'Некорректный адрес страницы авторизации'

    def click_become_a_client(self):
        become_a_client_button = self.browser.find_element(*MainPageLocators.BECOME_A_CLIENT)
        become_a_client_button.click()

    def click_order_a_debt_card(self):
        order_a_debt_card_button = self.browser.find_element(*MainPageLocators.ORDER_A_DEBT_CARD_BUTTON)
        order_a_debt_card_button.click()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(OrderADebtCardLocators.
                                                                             NAME_FIELD))
        self.browser.find_element(*OrderADebtCardLocators.NAME_FIELD)
        self.browser.execute_script("window.scrollTo(0, 700)")
        order_a_debt_card_link = self.browser.current_url
        self.browser.get_screenshot_as_file("C:\\Users\\kappa\\PycharmProjects\\Gazprombank_ru_autotests"
                                            "\\ScreenShots\\debt_card_order.png")

        assert '/personal/cards/' in order_a_debt_card_link, "Некорректный адрес страницы оформления карты"

    def close_cookie_alert(self):
        close_cookie_btn = self.browser.find_element(*MainPageLocators.CLOSE_COOKIE)
        close_cookie_btn.click()
        # assert self.browser.find_element(*MainPageLocators.COOKIE_ALERT)

    def go_to_consumer_credit_page(self):
        pass

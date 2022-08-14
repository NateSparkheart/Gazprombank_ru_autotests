import time

from pages.locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_button = self.browser.find_element(*MainPageLocators.LOGIN_BUTTON)
        login_button.click()
        login_page_link = self.browser.current_url
        assert login_page_link == 'https://online.gpb.ru/login', 'Некорректный адрес страницы авторизации'

    def click_become_a_client(self):
        become_a_client_button = self.browser.find_element(*MainPageLocators.BECOME_A_CLIENT)
        become_a_client_button.click()

    def click_offer_a_debt_card(self):
        offer_a_debt_card_button = self.browser.find_element(*MainPageLocators.ORDER_A_DEBT_CARD_BUTTON)
        offer_a_debt_card_button.click()
        time.sleep(10)
        offer_a_debt_card_link = self.browser.current_url
        assert '/personal/cards/' in offer_a_debt_card_link

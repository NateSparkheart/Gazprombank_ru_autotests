from pages.locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


locators = {
    'bank_project_switcher': 'div > svg > g > path:nth-child(1)',
    'private_client_link': 'div.main_root__wrapper_block--1aa82.main_left--1aa82 > a > svg',
     'bullshit_button': 'trash > selector'
}


class MainPage(BasePage):
    def go_to_login_page(self):
        login_button = self.browser.find_element(*MainPageLocators.LOGIN_BUTTON)
        login_button.click()

    def should_be_correct_login_url(self):
        login_page_link = self.browser.current_url
        assert login_page_link == 'https://online.gpb.ru/login', 'Некорректный адрес страницы авторизации'

    def element_is_presented_on_page(self):
        for k, v in locators.items():
            assert self.is_element_present(By.CSS_SELECTOR, v), 'Элемент ' + str(k) + ' отсутствует'

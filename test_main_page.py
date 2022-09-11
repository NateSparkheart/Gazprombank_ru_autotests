from pages.main_page import MainPage
from pages.locators import MainPageLocators


link = "https://www.gazprombank.ru/"


def test_guest_can_go_to_login_page(browser):  #11/09
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_main_page_ui_elements_are_presented(browser):  #11/09
    page = MainPage(browser, link)
    page.open()
    page.elements_are_presented_on_page(MainPageLocators.main_page_ui_elements_locators)


def test_guest_can_go_to_offer_a_debt_card_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.click_become_a_client()
    page.click_offer_a_debt_card()

# Дописать, не проверяет "исчезновение"
def test_cookie_alert_can_be_closed(browser):
    page = MainPage(browser, link)
    page.open()
    page.close_cookie_alert()








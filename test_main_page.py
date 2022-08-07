from pages.main_page import MainPage


link = "https://www.gazprombank.ru/"
# Посетитель сайта может попасть на страницу авторизации
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_correct_login_url()


def test_ui_elements_are_presented(browser):
    page = MainPage(browser, link)
    page.open()
    page.element_is_presented_on_page()



from pages.locators import MainPageLocators
from selenium.common.exceptions import NoSuchElementException, WebDriverException

class BasePage:
    def __init__(self, browser, url, timeout=5):  # конструктор
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)  # метод перехода по ссылке

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException, WebDriverException):
            return False
        return True

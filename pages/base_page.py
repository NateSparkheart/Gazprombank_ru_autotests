from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser, url, timeout=5):  # конструктор
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException, WebDriverException):
            return False
        return True

    def elements_are_presented_on_page(self, d):
        for k, v in d.items():
            assert self.is_element_present(By.CSS_SELECTOR, v), 'Элемент ' + str(k) + ' отсутствует'
            continue


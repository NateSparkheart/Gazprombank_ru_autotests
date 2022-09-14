import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import OrderADebtCardLocators
import random


class DebtCardPage(BasePage):
    def order_a_card(self):
        name = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(OrderADebtCardLocators.NAME_FIELD))
        name.send_keys('Сергеев Сергей Сергеевич')
        phone = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(OrderADebtCardLocators.PHONE_NUMBER_FIELD))
        phone.send_keys(random.randint(9000000000, 9999999999))
        time.sleep(2)
        mail = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(OrderADebtCardLocators.
                                                                                    EMAIL_FIELD))
        mail.send_keys(('test_mail' + str(random.randint(1, 100)) + '@gmail.com'))
        self.browser.find_element(*OrderADebtCardLocators.NEXT_STEP_BUTTON).click()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(OrderADebtCardLocators.
                                                                             SMS_CODE_FIELD))
        self.browser.execute_script("window.scrollTo(0, 850)")
        assert self.is_element_present(
            *OrderADebtCardLocators.SMS_CODE_FIELD), 'Поле для ввода кода из СМС отсутствует'
        self.browser.get_screenshot_as_file("C:\\Users\\kappa\\PycharmProjects\\Gazprombank_ru_autotests"
                                            "\\ScreenShots\\sms_code.png")



import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import OrderADebtCardLocators
import random


class DebtCardPage(BasePage):
    def request_a_card(self):
        name = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(OrderADebtCardLocators.NAME_FIELD))
        name.send_keys('Смирнов Сергей Дмитриевич')
        time.sleep(1)

        phone = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(OrderADebtCardLocators.PHONE_NUMBER_FIELD))
        phone.send_keys(random.randint(9000000000, 9999999999))
        time.sleep(1)

        mail = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(OrderADebtCardLocators.
                                                                                    EMAIL_FIELD))
        mail.send_keys(('test_mail' + str(random.randint(1, 100)) + '@gmail.com'))
        time.sleep(1)

        next_step = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(OrderADebtCardLocators.
                                                                                         NEXT_STEP_BUTTON))

        next_step.click()
        time.sleep(1)

        sms_field = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(OrderADebtCardLocators.
                                                                                         SMS_CODE_FIELD))
        time.sleep(1)
        assert self.is_element_present(
            *OrderADebtCardLocators.SMS_CODE_FIELD), 'Поле для ввода кода из СМС отсутствует'

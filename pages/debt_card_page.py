from pages.base_page import BasePage
from pages.locators import OrderADebtCardLocators
import faker


class DebtCardPage(BasePage):
    def request_a_card(self):
        f = faker.Faker
        name = f.name()



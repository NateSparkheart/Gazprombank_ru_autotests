from pages.debt_card_page import DebtCardPage

link = 'https://www.gazprombank.ru/personal/cards/6731473#first-step'


def test_guest_can_order_a_card(browser):
    page = DebtCardPage(browser, link)
    page.open()
    page.order_a_card()

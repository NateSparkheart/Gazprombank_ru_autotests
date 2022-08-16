from selenium.webdriver.common.by import By


class MainPageLocators:
    main_page_ui_elements_locators = {
        'bank_project_switcher': 'div > svg > g > path:nth-child(1)',
        'private_client_link': 'div.main_root__wrapper_block--1aa82.main_left--1aa82 > a > svg',
        'login_button': 'div.main_root__entry_links--1aa82 > a',
        'client_switcher': 'div.main_root__sections--1aa82.intersection_wrapper_root--b657c'
                           '.intersection_wrapper_mount--b657c > div > div > div > svg',
        'location': 'div.main_root__wrapper_block--1aa82.main_right--1aa82 > div:nth-child(1) > span',
        'offices and ATMs': 'div.main_root__wrapper_block--1aa82.main_right--1aa82 > div:nth-child(2)'
                            '> a:nth-child(1)',
        'become_a_client': 'div:nth-child(1) > div:nth-child(1) > div > div > button > span',
        'suspicious_button': 'lame > selector',
    }

    LOGIN_BUTTON = (By.CSS_SELECTOR, main_page_ui_elements_locators['login_button'])
    BECOME_A_CLIENT = (By.CSS_SELECTOR, main_page_ui_elements_locators['become_a_client'])
    ORDER_A_DEBT_CARD_BUTTON = (By.CSS_SELECTOR, '#tippy-2 > div > div > div > div > div > div > a:nth-child(2)'
                                '> div > div.popup_links_root__block--8eeef')


class OrderADebtCardLocators:
    NAME_FIELD = (By.CSS_SELECTOR, 'div.nr-step-form-fields > div:nth-child(2) > div > input')
    PHONE_NUMBER_FIELD = (By.CSS_SELECTOR, 'div.nr-step-form-fields > div:nth-child(3) > div > input')
    EMAIL_FIELD = (By.CSS_SELECTOR, 'div.nr-step-form-fields > div:nth-child(4) > div > input')
    NEXT_STEP_BUTTON = (By.CSS_SELECTOR, ' div.nr-step-form-sms > button')
    SMS_CODE_FIELD = (By.CSS_SELECTOR, '#sms_code')
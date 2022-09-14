from selenium.webdriver.common.by import By


class MainPageLocators:
    main_page_ui_elements_locators = {
        'bank_project_switcher': 'div > svg > g > path:nth-child(1)',
        'private_client_link': '.header_full_main_menu_active--1aa82.intersection_wrapper_visible--b657c',
        'login_button': '.header_full_main_menu_root__entry_links--1aa82',
        'client_switcher': '.intersection_sub_menu_sub_menu__icon--380c7',
        'location': '.header_full_main_menu_root__item_city--1aa82',
        'offices and ATMs': '.header_full_main_menu_root__item_link--1aa82',
        'become_a_client': '.header_full_bottom_popups_popups__cell--8cf97:first-of-type',
        #'suspicious_button': 'lame > selector',
        #'promo': '.nr-banners-control',
        'cookie_alert': '.cookie_accept_root__content--df898',
        'credit_list': 'div.header_full_menu_item_menu_item__name--f3bff.header_full_menu_item_open--f3bff'
    }

    LOGIN_BUTTON = (By.CSS_SELECTOR, main_page_ui_elements_locators['login_button'])
    BECOME_A_CLIENT = (By.CSS_SELECTOR, main_page_ui_elements_locators['become_a_client'])
    ORDER_A_DEBT_CARD_BUTTON = (By.CSS_SELECTOR, '.header_full_popup_links_root__wrapper--8eeef ['
                                                 'href="/personal/cards/6731473#first-step"]')
   # PROMO_BANNER = (By.CSS_SELECTOR, main_page_ui_elements_locators['promo'])
    COOKIE_ALERT = (By.CSS_SELECTOR, main_page_ui_elements_locators['cookie_alert'])
    CLOSE_COOKIE = (By.CSS_SELECTOR, '.cookie_accept_root__cross--df898')
    CREDIT_LIST = (By.CSS_SELECTOR, main_page_ui_elements_locators['credit_list']) ## Делаем проверку потр кредита + кукей


class OrderADebtCardLocators:
    NAME_FIELD = (By.CSS_SELECTOR, '.nr-step-form-fields__dadata [name="fio"]')
    PHONE_NUMBER_FIELD = (By.CSS_SELECTOR, '.form_phone_root__input--e053c')
    EMAIL_FIELD = (By.CSS_SELECTOR, '.nr-step-form-fields__dadata [name="email"]')
    NEXT_STEP_BUTTON = (By.CSS_SELECTOR, 'div.nr-step-form-sms > button')
    SMS_CODE_FIELD = (By.CSS_SELECTOR, '#sms_code')
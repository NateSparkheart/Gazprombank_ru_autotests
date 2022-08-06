import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Выберите браузер для тестов: Chrome либо Firefox")
    parser.addoption('--language', action='store', default='ru',
                     help="Выберите язык для тестов: (ru, en, etc..)")


@pytest.fixture(scope="function")
def browser(request):

    browser_name = request.config.getoption("browser_name")
    ui_language = request.config.getoption("language")

    if browser_name == "chrome":
        print("\nЗапуск Google Chrome для теста")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': ui_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nЗапуск Mozilla Firefox для теста")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", ui_language)
        browser = webdriver.Firefox(firefox_profile=fp)

    yield browser

    print("\nЗакрываем браузер")

    browser.quit()

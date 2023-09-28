import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en, fr or something else")

@pytest.fixture(scope="function")
def browser(request):

    language = request.config.getoption("language")

    if language is not None:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)
    else:
        raise pytest.UsageError("please choose a language, for example: --language=jp")
    yield browser
    print("\nquit browser..")
    browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"

def test_guest_should_see_add_item_button(browser):
    browser.get(link)
    selector = "button.btn"
    button = browser.find_elements(By.CSS_SELECTOR, f"{selector}")

    assert button, f"No such element '{selector}'"



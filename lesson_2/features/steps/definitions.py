from behave import step, when, given, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep
from random import randint

@given('Navigate to eBay via Chrome')
def open_website(browser):
    browser.driver = webdriver.Chrome()
    browser.driver.get("https://www.ebay.com/")
    browser.driver.maximize_window()

@step('Enter "iPhone" in searchfield')
def item_search(browser):
    input_field = browser.driver.find_element(By.XPATH, '//input[@id="gh-ac"]')
    input_field.send_keys("iPhone", Keys.ENTER)
    sleep(2);


@when('Click on the random element picture from the list')
def select_element(browser):
    """
    select random element from searched list and pick it
    """
    list_products_elements = browser.driver.find_elements(By.XPATH, "//ul[contains(@class, 'srp-list')]/li[contains(@class, 's-item')]")
    # random_element = list_products_elements[0]
    random_element = list_products_elements[randint(0, len(list_products_elements))]
    clickable_img = random_element.find_element(By.XPATH, './div/div[contains(@class, "s-item__image-section")]')
    clickable_img.click()

@step('Switch the browsers tab')
def switch_browsers_tab(browser):
    """
    Switch to the last opened tab in the browser
    """
    tabs = browser.driver.window_handles
    browser.driver.switch_to.window(tabs[-1])

@step('Product customization dropdown elements randomly selected')
def select_dropdown_elements(browser):
    select_elements = browser.driver.find_elements(By.XPATH, '//select[@class="x-msku__select-box"]')
    for element in select_elements:
        select = Select(element)
        select.select_by_index(1)
        sleep(3)

@step('Click on Add to cart')
def add_to_cart(browser):
    add_to_cart_btn = browser.driver.find_element(By.XPATH, '//a[contains(@class, "fake-btn") and contains(@href, "cart")]')
    add_to_cart_btn.click()
    sleep(3)

@step('Refresh the page and go to cart')
def refresh_to_cart(browser):
    browser.driver.refresh()
    cart_icon = browser.driver.find_element(By.XPATH, '//ul[@id="gh-eb"]/li[@id="gh-minicart-hover"]')
    cart_icon.click()
    sleep(5)

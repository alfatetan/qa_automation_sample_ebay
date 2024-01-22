from behave import step, when, given, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

class Links:
    """
    This class contains the paths to the nodes of elements
    """
    @staticmethod
    def top_menu(menu_item):
        return f'//div[@id="gh-top"]/ul/li/descendant::a[contains(text(), "{menu_item}")]'
    # @staticmethod
    # def links_list():
    #     return f'//div[@id="gh-top"]/ul/descendant::li/a[not(text()="")]'
    

@step('Click on menu item {menu_item}')
def click_menu_item(browser, menu_item="Sell"):
    element = browser.driver.find_element(By.XPATH, Links.top_menu(menu_item))
    element.click()

@given('Navigate to {url}')
def navigate_website(browser, url):
    browser.driver = webdriver.Chrome()
    browser.driver.get(url)
    browser.driver.maximize_window()

@step('Page exists')
def page_avaliability_check(browser):
    title = browser.driver.title.lower()
    if 'error' in title:
        assert False, "!!! The page is not available !!!"
    elif 'security' in title:
        assert False, "!!! Impossible to check - CAPTCHA !!!"


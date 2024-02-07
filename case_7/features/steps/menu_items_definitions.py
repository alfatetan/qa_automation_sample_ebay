from behave import step, when, given, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep



@step('Click on menu item "{menu_item}"')
def click_menu_item(browser, menu_item="Sell"):
    xpath_menu_item = f'//div[@id="gh-top"]/ul/li/descendant::a[contains(text(), "{menu_item.strip()}")]'
    try:
        element = browser.driver.find_element(By.XPATH, xpath_menu_item)
        element.click()
    except:
        raise Exception(f'Could not find menu element "{menu_item}" on the page')
    
@step('Page should contain "{keyword}" in the header')
def header_verification(browser, keyword):
    # If page container doesn't contain the keyword then desired page does not exists
    xpath = f'//div[@class="pagecontainer__top"]//*[contains(text(),"{keyword}")]'
    elements = browser.driver.find_elements(By.XPATH, xpath)

    if not elements:
        raise Exception(f'The page is not matching. The header does not contain {keyword}')
    
@step('Main menu item in "{level}" level "{desired_menu_item}" is clicked')
def click_main_menu_item(browser, level, desired_menu_item):
    
    # Choose the menu level
    if level == "root":
        menu_xpath = '//ul[@class="vl-flyout-nav__container"]/li[not(contains(@class, "js-more-show"))]/a'
    elif level == "submenu":
        menu_xpath = '//ul[@class="vl-flyout-nav__container"]/li[not(contains(@class, "js-more-show")) and a]//nav[@class="vl-flyout-nav__sub-cat-col"]//li/a'
    # Grab all "a" tags from required menu level
    menu_links = browser.driver.find_elements(By.XPATH, menu_xpath)
    # Find menu item from the list and click on it
    for el in menu_links:
        menu_item_text = el.get_attribute('text')
        if desired_menu_item.lower() in menu_item_text.strip().lower():
            uri = el.get_attribute('href')
            browser.driver.get(uri)
            return
    raise Exception(f"!!! Menu item was not found !!!")
    

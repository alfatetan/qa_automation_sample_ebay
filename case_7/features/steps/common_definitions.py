from behave import step, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

@step('Navigate to the "{url}"')
def start_browser(browser, url):
    """
    Open a browser with the specified webpage URL
    """
    browser.driver = webdriver.Chrome()
    browser.driver.get(url)

@step('Maximize browser window')
def maximize_window(browser):
    browser.driver.maximize_window()

@step('Page exists')
def page_avaliability_check(browser):
    title = browser.driver.title.lower()
    if 'error' in title:
        assert False, "!!! The page is not available !!!"
    elif 'security' in title:
        assert False, "!!! Impossible to check - CAPTCHA !!!"

#Then Page title contains "<PAGE_TITLE>"
@step('Page title contains "{page_title}"')
def page_title_matching(browser, page_title):
    # Check if page is existing
    page_avaliability_check(browser)
    
    # If page exists, check the title
    title = browser.driver.title.lower()
    error_msg = f"!!! Page title does not contain required text !!! \n"\
                f"Required text: {page_title} not contains in the \n"\
                f"Page title: {title}"
    assert page_title.lower() in title, error_msg
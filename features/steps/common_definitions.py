from behave import step, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

@step('Navigate to the eBay')
def start_context(context):
    """
    Open a context with the specified webpage URL
    """
    context.driver.get(context.URL)
    # check if webpage uploaded correctly
    headers = Wait(context.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//h2[@class="vl-card-header__headline"]')), message="!!! MAIN PAGE DOES NOT APPEAR HERE !!!")


@step('Maximize browser window')
def maximize_window(context):
    context.driver.maximize_window()

@step('Page exists')
def page_avaliability_check(context):
    title = context.driver.title.lower()
    if 'error' in title:
        assert False, "!!! The page is not available !!!"
    elif 'security' in title:
        assert False, "!!! Impossible to check - CAPTCHA !!!"

#Then Page title contains "<PAGE_TITLE>"
@step('Page title contains "{page_title}"')
def page_title_matching(context, page_title):
    # Check if page is existing
    page_avaliability_check(context)
    
    # If page exists, check the title
    title = context.driver.title.lower()
    error_msg = f"!!! Page title does not contain required text !!! \n"\
                f"Required text: {page_title} not contains in the \n"\
                f"Page title: {title}"
    assert page_title.lower() in title, error_msg


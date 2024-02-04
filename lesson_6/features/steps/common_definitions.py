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
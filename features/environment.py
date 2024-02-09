from selenium import webdriver
import re
from datetime import datetime as dt

# def before_all():
#     pass

def before_feature(browser, feature):
    browser.URL = 'https://ebay.com'

def before_scenario(browser, scenario):
    browser.driver = webdriver.Chrome()

# def before_step(browser, step):
#     pass

def after_step(browser, step):
    # if step is filed take a screenshot
    if step.status == 'failed':
        # filename format as a step name through underscores space
        screenshot_name = '_'.join(re.findall('\w+', step.name))
        filename = f'{dt.now().strftime("%Y-%m-%d_%H:%M:%S")}_{screenshot_name}.png'
        browser.driver.save_screenshot(f'./reports/screenshots/{filename}')

def after_scenario(browser, scenario):
    # close window
    browser.driver.close()
    # quit the chrome driver
    browser.driver.quit()

# def after_feature(browser, feature):
#     pass

# def after_all():
#     pass
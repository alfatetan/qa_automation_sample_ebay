from selenium import webdriver
import re
from datetime import datetime as dt

# def before_all():
#     pass

def before_feature(context, feature):
    context.URL = 'https://ebay.com'

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    # Add the implicitly waiting
    context.driver.implicitly_wait(3)

# def before_step(context, step):
#     pass

def after_step(context, step):
    # if step is filed take a screenshot
    if step.status == 'failed':
        # filename format as a step name through underscores space
        screenshot_name = '_'.join(re.findall('\w+', step.name))
        filename = f'{dt.now().strftime("%Y-%m-%d_%H:%M:%S")}_{screenshot_name}.png'
        context.driver.save_screenshot(f'./reports/screenshots/{filename}')

def after_scenario(context, scenario):
    # close window
    context.driver.close()
    # quit the chrome driver
    context.driver.quit()

# def after_feature(context, feature):
#     pass

# def after_all():
#     pass
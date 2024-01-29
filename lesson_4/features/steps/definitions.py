from behave import step, when, then, given
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

@given('Navigate to the "{url}"')
def navigate(browser, url):
    browser.driver = webdriver.Chrome()
    browser.driver.get(url)
    browser.driver.maximize_window()
    sleep(1)

# When Type "iPhone" to searchfield
@step('Enter "{item}" to searchfield')
def searchfield(browser, item):
    searchfield = browser.driver.find_element(By.XPATH, '//input[contains(@aria-label, "Search for anything")]')
    searchfield.send_keys(item)
    searchfield.send_keys(Keys.ENTER)
    sleep(3)

# Then All results contain "iPhone"
@step('All results contain "{item}"')
def check_all_search_results(browser, item):
    # Parse all results after searching
    search_results = browser.driver.find_elements(By.XPATH, '//ul[contains(@class, "srp-results")]/li[@id]')
    # Check one-by-one result - does it have the keyword or not
    errors_id_list = []
    for el in search_results:
        # Check a title of the searching element
        title = el.find_element(By.XPATH, './/div[@class="s-item__title"]/span')
        el_id = el.get_property('id')
        if item.lower() not in title.text.lower():
            errors_id_list.append(el_id)
    # assert item.lower() not in title.text.lower(), f"Position id = {el_id} does not contain searching expression {item}"
    assert not errors_id_list, f"The next elements with ids have errors {errors_id_list}"
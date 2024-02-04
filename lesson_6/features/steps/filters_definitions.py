from behave import step, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

@step('Enter "{item}" to searchfield')
def searchfield(browser, item):
    """
    Obtain the search results
    """
    searchfield = browser.driver.find_element(By.XPATH, '//input[contains(@aria-label, "Search for anything")]')
    searchfield.send_keys(item)
    searchfield.send_keys(Keys.ENTER)

# When "<OPTION>" is selected from "<FILTER>"
@step('"{required_option}" is selected from "{required_filter}"')
def filter_selecting(browser, required_option, required_filter):
    """
    Select the required option in particularly filter
    IN : required_filter, required_option
    OUT : Action - webdriver clicks on the required option in required filter
    """
    # Parse all filters
    filters = browser.driver.find_elements(By.XPATH, '//ul[@class="x-refine__left__nav"]/li/ul/li')
    # Find the required filter that match with required title
    for filter in filters:
        title = filter.find_element(By.XPATH, './/div[@class="x-refine__item__title-container"]').text
        if title.lower() == required_filter.lower():
            # Parse all filter options if title matches filter
            filter_options = filter.find_elements(By.XPATH, './/div[@class="x-refine__select__svg"]')
            # Search the required option
            for option in filter_options:
                option_title = option.find_element(By.XPATH, './/span[contains(@class, "x-refine__multi-select-cbx")]').text.split('\n')[0]
                # Select required option
                if option_title.lower() == required_option.lower():
                    checkbox = option.find_element(By.XPATH, './/input[@type="checkbox"]')
                    checkbox.click()                   
                    # Interrupt the loops
                    break
            break    


# Then "<KEYWORD>" should be in the items title
@step('"{keywords}" should be in the items title')
def keyword_verification(browser, keywords):
    # Parse all keywords in the list
    all_keywords = keywords.split(":")
    # Parse all elements after filtering
    all_results = browser.driver.find_elements(By.XPATH, '//ul[contains(@class, "srp-results")]/li[@id]')
    # All errors should be saved in the list
    errors_list = []
    # One by one verifying all titles for keyword inclusion
    for el in all_results:
        # Check a title of the searching element
        title = el.find_element(By.XPATH, './/div[@class="s-item__title"]/span')
        el_id = el.get_property('id')
        # Count on the default that error is
        error = True
        for keyword in all_keywords:
            # if one of keywords is matching with title text the error does not exist
            if keyword.lower().strip() in title.text.lower():
                error = False
        # add the error list if error exists
        if error:
            errors_list.append([el_id, title.text])
    assert not errors_list, f"The next elements with ids have errors {errors_list}"



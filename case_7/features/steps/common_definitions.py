from behave import step, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint

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

@step ('Turn to page "{desired_page}"')
def turn_to_page(browser, desired_page):
    """
    IN: desired_page - number of page [int] || "next", "previous" or "random" [string]
    OUT: desired page is selected
    """
    pages_range_els = browser.driver.find_elements(By.XPATH, '//ol[@class="pagination__items"]/li[not(@hidden)]/a')
    next_page_el = browser.driver.find_element(By.XPATH, '//*[@type="next"]')
    first_page = int(pages_range_els[0].text)
    last_page = int(pages_range_els[-1].text)
    
    try:
        desired_page = int(desired_page)
        # go to needed range pages (avoid step by step)
        while (desired_page not in range(first_page, last_page + 1)):
            # check if our page does not exist in the last range
            try:
                next_page_el = browser.driver.find_element(By.XPATH, '//*[@type="next"]')
            except:
                raise ValueError(f"!!! The page #{desired_page} does not exist in the range !!!")
            # shift the pages range
            pages_range_els[last_page - 1].click()
            # refresh the page's data
            pages_range_els = browser.driver.find_elements(By.XPATH, '//ol[@class="pagination__items"]/li[not(@hidden)]/a')
            first_page = int(pages_range_els[0].text)
            last_page = int(pages_range_els[-1].text)
        # When the range is searched we choose our desired page and click on it
        for page in pages_range_els:
            if int(page.text) == desired_page:
                page.click()
        return
    except:
        if desired_page == "random":
        # The turn to the random page is implemented as a random page
        # from the current list of pages (the range of 10 pages). It's
        # possible to use random numbers from all pages; however, we should
        # parse all of them. It takes time to test. I decided to cut this
        # function for several pages, which is enough for the test project
        # to show the logic only.
            random_page = randint(first_page, last_page + 1)
            pages_range_els[random_page - 1].click()
        elif desired_page == "next":
            next_page_el.click()
        elif desired_page == "previous":
            prev_page_el = browser.driver.find_element(By.XPATH, '//*[@type="previous"]')
            prev_page_el.click()
        elif type(desired_page) is not int:
            raise ValueError("!!! Not accessible function parameter - number of page: (turn_to_page function) !!!")
    
    
@step('Do on pages from "{start_pg}" to "{end_pg}" next steps')
def do_on_pages(browser, start_pg, end_pg):
    try:
        start_pg = int(start_pg)
        end_pg = int(end_pg)
        page_range = range(start_pg, end_pg+1) if end_pg > start_pg else range(end_pg, start_pg+1)
    except:
        raise ValueError("!!! Use the digits only in the step 'Do on page' !!!")
    
    for page in page_range:
        execute = f'When Turn to page "{page}"'
        browser.execute_steps(f'''
            When Turn to page "{page}"
        ''')
        for step_row in browser.table.rows:
            # parse the steps and execute them
            step_dict = step_row.as_dict()
            step = step_dict['Steps']
            browser.execute_steps(step)

@step('For all pages')
def for_all_pages(browser):
    while (True):
        current_page = int(browser.driver.find_element(By.XPATH, '//ol[@class="pagination__items"]/li/a[@aria-current]').text)
        pages_range_els = browser.driver.find_elements(By.XPATH, '//ol[@class="pagination__items"]/li[not(@hidden)]/a')
        last_page = int(pages_range_els[-1].text)
        
        for step_row in browser.table.rows:
            # parse the steps and execute them
            step_dict = step_row.as_dict()
            step = step_dict['Steps']
            browser.execute_steps(step)
        next_page_el = browser.driver.find_element(By.XPATH, '//*[@type="next"]')

        if current_page == last_page:
            break
        else:
            next_page_el.click()
        
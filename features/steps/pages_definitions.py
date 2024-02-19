from behave import step, when, given, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from random import randint

@step ('Turn to page "{desired_page}"')
def turn_to_page(context, desired_page):
    """
    IN: desired_page - number of page [int] || "next", "previous" or "random" [string]
    OUT: desired page is selected
    """
    pages_range_els = context.driver.find_elements(By.XPATH, '//ol[@class="pagination__items"]/li[not(@hidden)]/a')
    next_page_el = context.driver.find_element(By.XPATH, '//*[@type="next"]')
    first_page = int(pages_range_els[0].text)
    last_page = int(pages_range_els[-1].text)
    
    try:
        desired_page = int(desired_page)
        # go to needed range pages (avoid step by step)
        while (desired_page not in range(first_page, last_page + 1)):
            # check if our page does not exist in the last range
            # ----------------------------------------------------------------
            # try:
            #     next_page_el = context.driver.find_element(By.XPATH, '//a[@type="next"]')
            # except:
            #     raise ValueError(f"!!! The page #{desired_page} does not exist in the range !!!")
            # ----------------------------------------------------------------
            # instead of previous construction we can use the next expression:
            next_page_el = Wait(context.driver, 3).until(EC.presence_of_element_located(
                    (By.XPATH, '//a[@type="next"]')), message=f"!!! The page #{desired_page} does not exist in the range !!!")
            # shift the pages range
            pages_range_els[last_page - 1].click()
            # refresh the page's data
            pages_range_els = context.driver.find_elements(By.XPATH, '//ol[@class="pagination__items"]/li[not(@hidden)]/a')
            first_page = int(pages_range_els[0].text)
            last_page = int(pages_range_els[-1].text)
        # When the range is searched we choose our desired page and click on it
        for page in pages_range_els:
            if int(page.text) == desired_page:
                page.click()
                break
    except:
        # The turn to the random page is implemented as a random page
        # from the current list of pages (the range of 10 pages). It's
        # possible to use random numbers from all pages; however, we should
        # parse all of them. It takes time to test. I decided to cut this
        # function for several pages, which is enough for the test project
        # to show the logic only.
        if desired_page == "random":
            random_page = randint(first_page, last_page + 1)
            pages_range_els[random_page - 1].click()
        elif desired_page == "next":
            next_page_el.click()
        elif desired_page == "previous":
            prev_page_el = context.driver.find_element(By.XPATH, '//*[@type="previous"]')
            prev_page_el.click()
        elif int(desired_page):
            raise ValueError("!!! This page does not exist !!!")
        # elif type(desired_page) is not int:
        else:
            raise ValueError("!!! Not accessible function parameter - number of page: (turn_to_page function) !!!")
    
    
@step('Do on pages from "{start_pg}" to "{end_pg}" next steps')
def do_on_pages(context, start_pg, end_pg):
    try:
        start_pg = int(start_pg)
        end_pg = int(end_pg)
        page_range = range(start_pg, end_pg+1) if end_pg > start_pg else range(end_pg, start_pg+1)
    except:
        raise ValueError("!!! Use the digits only in the step 'Do on page' !!!")
    
    for page in page_range:
        context.execute_steps(f'''
            When Turn to page "{page}"
        ''')
        for step_row in context.table.rows:
            # parse the steps and execute them
            step_dict = step_row.as_dict()
            step = step_dict['Steps']
            context.execute_steps(step)

@step('For all pages')
def for_all_pages(context):
    while (True):
        current_page = int(context.driver.find_element(By.XPATH, '//ol[@class="pagination__items"]/li/a[@aria-current]').text)
        pages_range_els = context.driver.find_elements(By.XPATH, '//ol[@class="pagination__items"]/li[not(@hidden)]/a')
        last_page = int(pages_range_els[-1].text)
        
        for step_row in context.table.rows:
            # parse the steps and execute them
            step_dict = step_row.as_dict()
            step = step_dict['Steps']
            context.execute_steps(step)
        next_page_el = context.driver.find_element(By.XPATH, '//*[@type="next"]')

        if current_page == last_page:
            break
        else:
            next_page_el.click()

        
Feature: Header navigation checking

    Background:
        Given Navigate to the eBay
        And Maximize browser window
    
    # We can also use Scenario Outline style for our test cases
    # Scenario Outline: Check the header navigation elements
    #     When Click on menu item "<MENU_ITEM>"
    #     Then Page title contains "<PAGE_TITLE>"

    # Examples:
    #     | MENU_ITEM   | PAGE_TITLE                   |
    #     | Sign in     | Sign In or Register          |
    #     | register    | Create a personal account    |
    #     | Daily Deals | Best deals and Free Shipping |
    #     | Gift Cards  | Something                    |


    Scenario: Check the header navigation Sign In
        When Click on menu item "Sign in"
        Then Page title contains "Sign in or Register"

    Scenario: Check the header navigation "Register"
        When Click on menu item "register"
        Then Page title contains "Create a personal account"

    Scenario: Check the header navigation "Daily Deals"
        When Click on menu item "Daily Deals"
        Then Page title contains "Best deals and Free Shipping"

    Scenario: Check the header navigation "Gift Cards"
        When Click on menu item "Gift Cards"
        Then Page title contains "Gift Cards"

    Scenario: Check the header navigation "Help & Contacts"
        When Click on menu item "Help & Contact"
        Then Page title contains "Customer Service"

    Scenario: Check the header navigation "Sell"
        When Click on menu item "Sell"
        Then Page title contains "Selling on eBay"

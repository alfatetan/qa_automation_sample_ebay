Feature: Header navigation checking

    Scenario Outline: Check the header navigation elements
        Given Navigate to the "https://ebay.com"
        And Maximize browser window
        When Click on menu item "<MENU_ITEM>"
        Then Page title contains "<PAGE_TITLE>"

    Examples:
        | MENU_ITEM   | PAGE_TITLE                   |
        | Sign in     | Sign In or Register          |
        | register    | Create a personal account    |
        | Daily Deals | Best deals and Free Shipping |
        | Gift Cards  | Something                    |

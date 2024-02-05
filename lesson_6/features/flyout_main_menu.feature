Feature: Test main flyout menu items

    Scenario Outline: Test the root level flyout menu items
        Given Navigate to the "https://ebay.com"
        And Maximize browser window
        When Main menu item in "root" level "<MENU_ITEM>" is clicked
        And Page exists
        Then Page should contain "<HEADER>" in the header

    Examples:
        | MENU_ITEM      | HEADER          |
        | Sporting Goods | Sporting Goods  |
        | Motors         | Motors          |
        | Fashion        | Clothing, Shoes |
        | Incredible     | Nonexist        |
Feature: Test main flyout menu items

    Background:
        Given Navigate to the eBay
        And Maximize browser window
    
    Scenario Outline: Test the root level flyout menu items in root level
        When Main menu item in "root" level "<MENU_ITEM>" is clicked
        And Page exists
        Then Page should contain "<HEADER>" in the header
    Examples:
        | MENU_ITEM      | HEADER          |
        | Sporting Goods | Sporting Goods  |
        | Motors         | Motors          |
        | Fashion        | Clothing, Shoes |

    Scenario Outline: Test the submenu level flyout menu items
        When Main menu item in "submenu" level "<MENU_ITEM>" is clicked
        And Page exists
        Then Page should contain "<HEADER>" in the header
    Examples:
        | MENU_ITEM   | HEADER      |
        | Motorcycles | Motorcycles |
        | LEGO        | LEGO        |
        | Video Games | Video Games |
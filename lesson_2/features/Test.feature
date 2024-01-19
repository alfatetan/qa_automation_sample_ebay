Feature: Ebay Regression Test
    
    Scenario: Add an item to the cart
        Given Navigate to eBay via Chrome
        When Enter "iPhone" in searchfield
        And Click on the random element picture from the list
        Then Switch the browsers tab
        When Product customization dropdown elements randomly selected
        And Click on Add to cart
        When Refresh the page and go to cart


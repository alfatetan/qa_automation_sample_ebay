Feature: Test search and filtering results on the ebay.com website

    Scenario: Test search results
        Given Navigate to the "https://ebay.com"
        When Enter "iPhone" to searchfield
        Then All results contain "iPhone"
    
    Scenario: Test search results
        Given Navigate to the "https://ebay.com"
        When Enter "dress" to searchfield
        Then All results contain "dress"
    
    Scenario: Test search results
        Given Navigate to the "https://ebay.com"
        When Enter "headphones" to searchfield
        Then All results contain "headphones"
    
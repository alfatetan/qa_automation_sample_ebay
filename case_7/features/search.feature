Feature: Searching results verification

    Scenario Outline: The keyword comparison
        Given Navigate to the "https://ebay.com"
        And Maximize browser window
        When Enter "<ITEM>" to searchfield
        Then "<KEYWORDS>" should be in the items title

    # Use a colon (:) to separate keywords
    Examples:
        | ITEM    | KEYWORDS                             |
        | Dress   | Dress: Robe : Strapless : Shirtdress |
        | CPU     | Intel : AMD : CPU                    |
        | Monitor | Monitor : Display                    |
        | Watch   | Watch                                |

Feature: Searching results verification

    Background:
        Given Navigate to the eBay
        And Maximize browser window

    Scenario Outline: The keyword comparison
        When Enter "<ITEM>" to searchfield
        Then "<KEYWORDS>" should be in the items title

    # Use a colon (:) to separate keywords
    Examples:
        | ITEM    | KEYWORDS                             |
        | Dress   | Dress: Robe : Strapless : Shirtdress |
        | CPU     | Intel : AMD : CPU                    |
        | Monitor | Monitor : Display                    |
        | Watch   | Watch                                |

# TODO: Searching on an opened item page
# TODO: Add scenario for each item and set of keywords
# TODO: Searching on several pages
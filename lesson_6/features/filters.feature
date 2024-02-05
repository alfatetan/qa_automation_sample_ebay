Feature: Test filters with particular searching results

    @selective
    Scenario Outline: Check the obtained result using the filtering option
        Given Navigate to the "https://ebay.com"
        And Maximize browser window
        When Enter "<ITEM>" to searchfield
        When "<OPTION>" is selected from "<FILTER>"
        Then "<KEYWORDS>" should be in the items title
    
    # Use semicolon (:) to separate the keywords
    Examples:
        | ITEM     | FILTER             | OPTION      | KEYWORDS                  |
        | Memory   | Type               | DDR4 DRAM   | DDR4 : DDR 4              |
        | Memory   | Total Capacity     | 32 GB       | 32GB : 32 GB : 32G : 32 G |
        | Monitor  | Maximum Resolution | 3440 x 1440 | 3440x1440 : 2440 x 1440   |
        | Monitor  | Refresh Rate       | 100 Hz      | 100Hz : 100 Hz            |
        | Keyboard | Brand              | Logitech    | Logitech                  |

Feature: Test filters with particular group of purchases

    Scenario Outline: Check the obtained result using the filtering option
        Given Navigate to the "https://ebay.com"
        When Enter "<ITEM>" to searchfield
        When "<OPTION>" is selected from "<FILTER>"
        Then "<KEYWORD>" should be in the items title
    
    Examples:
        | ITEM     | FILTER             | OPTION      | KEYWORD   |
        | Memory   | Type               | DDR4 DRAM   | DDR4      |
        | Memory   | Total Capacity     | 32 GB       | 32GB      |
        | Monitor  | Maximum Resolution | 3440 x 1440 | 3440x1440 |
        | Monitor  | Refresh Rate       | 100 Hz      | 100Hz     |
        | Keyboard | Brand              | Logitech    | Logitech  |

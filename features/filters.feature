Feature: Test filters with particular searching results
    Background:
        Given Navigate to the eBay
        And Maximize browser window

    Scenario Outline: Checking the filter on the first page
        When Enter "<ITEM>" to searchfield
        When "<OPTION>" is selected from "<FILTER>"
        Then "<KEYWORDS>" should be in the items title
    # Use a colon (:) to separate the keywords
    Examples:
        | ITEM     | FILTER             | OPTION      | KEYWORDS                  |
        | Memory   | Type               | DDR4 DRAM   | DDR4 : DDR 4              |
        | Memory   | Total Capacity     | 32 GB       | 32GB : 32 GB : 32G : 32 G |
        | Monitor  | Maximum Resolution | 3440 x 1440 | 3440x1440 : 2440 x 1440   |
        | Monitor  | Refresh Rate       | 100 Hz      | 100Hz : 100 Hz            |
        | Keyboard | Brand              | Logitech    | Logitech                  |


    Scenario Outline: Checking the filter on the second page
        When Enter "<ITEM>" to searchfield
        When "<OPTION>" is selected from "<FILTER>"
        And Turn to page "next"
        Then "<KEYWORDS>" should be in the items title
    # Use a colon (:) to separate the keywords
    Examples:
        | ITEM     | FILTER             | OPTION      | KEYWORDS                  |
        | Memory   | Type               | DDR4 DRAM   | DDR4 : DDR 4              |
        | Memory   | Total Capacity     | 32 GB       | 32GB : 32 GB : 32G : 32 G |
        | Monitor  | Maximum Resolution | 3440 x 1440 | 3440x1440 : 2440 x 1440   |
        | Monitor  | Refresh Rate       | 100 Hz      | 100Hz : 100 Hz            |
        | Keyboard | Brand              | Logitech    | Logitech                  |
    
    Scenario Outline: Checking the filter on the 13 page
        When Enter "<ITEM>" to searchfield
        When "<OPTION>" is selected from "<FILTER>"
        And Turn to page "13"
        Then "<KEYWORDS>" should be in the items title
    # Use a colon (:) to separate the keywords
    Examples:
        | ITEM     | FILTER             | OPTION      | KEYWORDS                  |
        | Keyboard | Brand              | Logitech    | Logitech                  |
        # | Memory   | Type               | DDR4 DRAM   | DDR4 : DDR 4              |
        # | Memory   | Total Capacity     | 32 GB       | 32GB : 32 GB : 32G : 32 G |
        # | Monitor  | Maximum Resolution | 3440 x 1440 | 3440x1440 : 2440 x 1440   |
        # | Monitor  | Refresh Rate       | 100 Hz      | 100Hz : 100 Hz            |

    Scenario Outline: Checking the filter on the random page
        When Enter "<ITEM>" to searchfield
        When "<OPTION>" is selected from "<FILTER>"
        And Turn to page "random"
        Then "<KEYWORDS>" should be in the items title
    # Use a colon (:) to separate the keywords
    Examples:
        | ITEM     | FILTER             | OPTION      | KEYWORDS                  |
        | Memory   | Type               | DDR4 DRAM   | DDR4 : DDR 4              |
        | Memory   | Total Capacity     | 32 GB       | 32GB : 32 GB : 32G : 32 G |
        | Monitor  | Maximum Resolution | 3440 x 1440 | 3440x1440 : 2440 x 1440   |
        | Monitor  | Refresh Rate       | 100 Hz      | 100Hz : 100 Hz            |
        | Keyboard | Brand              | Logitech    | Logitech                  |
    
    Scenario Outline: Checking the filter on the range page
        When Enter "<ITEM>" to searchfield
        When "<OPTION>" is selected from "<FILTER>"
        Then Do on pages from "2" to "4" next steps
            | Steps                                            |
            | Then "<KEYWORDS>" should be in the items title   |
    # Use a colon (:) to separate the keywords
    Examples:
        | ITEM     | FILTER | OPTION   | KEYWORDS |
        | CPU      | Brand  | Intel    | Intel    |
        | Keyboard | Brand  | Logitech | Logitech |

    Scenario Outline: Checking the filter on the range page back order
        When Enter "<ITEM>" to searchfield
        When "<OPTION>" is selected from "<FILTER>"
        Then Do on pages from "3" to "1" next steps
            | Steps                                            |
            | Then "<KEYWORDS>" should be in the items title   |  
    # Use a colon (:) to separate the keywords
    Examples:
        | ITEM | FILTER | OPTION | KEYWORDS |
        | CPU  | Brand  | Intel  | Intel    |

    Scenario Outline: Check the obtained result using the filtering option on the all pages
        When Enter "<ITEM>" to searchfield
        When "<OPTION>" is selected from "<FILTER>"
        And For all pages
            | Steps                                          |
            | Then "<KEYWORDS>" should be in the items title |
    # Use a colon (:) to separate the keywords
    Examples:
        | ITEM   | FILTER           | OPTION | KEYWORDS              |
        | iPhone | Storage Capacity | 1 TB   | iPhone : Apple        |
        | iPad   | Storage Capacity | 1 TB   | iPad : Apple : Tablet |
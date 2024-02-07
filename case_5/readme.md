# Lesson #5

Here we work with filters.

The paradigm of this test is to select the necessary filters and check the result against the expected result. This is the simplest way to do it.

**A real project would most likely require the use of more complex designs. Moreover, testing of filters should be done at the database level.**

My opinion is that filters should be checked at the database level and the obtained results should be checked with on FrontEnd part futher.

I used a template with the following examples:

| ITEM     | FILTER             | OPTION      | KEYWORD   |
| -------- | ------------------ | ----------- | --------- |
| Memory   | Type               | DDR4 DRAM   | DDR4      |
| Memory   | Total Capacity     | 32 GB       | 32GB      |
| Monitor  | Maximum Resolution | 3440 x 1440 | 3440x1440 |
| Monitor  | Refresh Rate       | 100 Hz      | 100Hz     |
| Keyboard | Brand              | Logitech    | Logitech  |

If the test is failed, the test report shows all items that do not meet the required filtering criteria, like the list of items [id, title]. E.g.:

File: report.txt

```python
  Scenario Outline: Check the obtained result using the filtering option -- @1.2   # features/filter.feature:12
    Given Navigate to the "https://ebay.com"                                       # features/steps/definitions.py:7
    When Enter "Memory" to searchfield                                             # features/steps/definitions.py:16
    When "32 GB" is selected from "Total Capacity"                                 # features/steps/definitions.py:26
    Then "32GB" should be in the items title                                       # features/steps/definitions.py:54
      Assertion Failed: The next elements with ids have errors [['item59ec94a93e', 'HyperX FURY DDR4 16GB 3200 MHz PC4-25600 Desktop RAM Memory DIMM 288pin 2x 16GB'], ['item44debc09f7', 'ADATA 16GB DDR4 SODIMM 3200MHz PC4-25600 CL22 260-pin Memory RAM Laptop'], ['item26c350e347', '4X8GB HMT41GU7BFR8A-PB SK HYNIX DDR3L KIT 1600MHZ ECC SERVER MEMORY A4-2'], ['item4049d57ec9', 'CRUCIAL DDR4 16GB 2x 3200 PC4-25600 Laptop SODIMM Non-ECC 260-Pin Memory RAM']]
```

If necessary, we can include regular expressions to specify searched keywords.

# Homework:

#### Scenario Outlines - convert existing repetitive TCs into Scenario Outline:

- [x] Header navigation links
- [x] Flyout menu (Motors / Electronics etc.)
- [x] Items search
- [x] Filters

#### While loop:

- [ ] Create scenario to validate filtering result on first several pages. Pagination must use while loop

:see_no_evil: **_Implemented in the next lesson (#7)_**

---

### Header navigation links

In the testing process the code compares a page's title with expected piece of text. If this title includes the text the test is considered passed.

### Filters and Search Results

A new feature was added where we can use several different filtering results. To use this feature, we need to use a semicolon separator (":") in a table like this:

```gherkin
    Examples:
        | ITEM     | FILTER             | OPTION      | KEYWORDS                  |
        | Memory   | Type               | DDR4 DRAM   | DDR4 : DDR 4              |
        | Memory   | Total Capacity     | 32 GB       | 32GB : 32 GB : 32G : 32 G |
        | Monitor  | Maximum Resolution | 3440 x 1440 | 3440x1440 : 3440 x 1440   |
        | Monitor  | Refresh Rate       | 100 Hz      | 100Hz : 100 Hz            |
        | Keyboard | Brand              | Logitech    | Logitech                  |
```

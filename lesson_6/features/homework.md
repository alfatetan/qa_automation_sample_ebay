# Homework:

#### Scenario Outlines - convert existing repetitive TCs into Scenario Outline:

- [ ] Header navigation links
- [ ] Flyout menu (Motors / Electronics etc.)
- [ ] Items search
- [x] Filters

#### While loop:

- [ ] Create scenario to validate filtering result on first several pages. Pagination must use while loop

---

## Filters

I added a new feature where we can use different filtering results. To use this feature we need to use a separator ":" in a table like this:

```gherkin
    Examples:
        | ITEM     | FILTER             | OPTION      | KEYWORDS                  |
        | Memory   | Type               | DDR4 DRAM   | DDR4 : DDR 4              |
        | Memory   | Total Capacity     | 32 GB       | 32GB : 32 GB : 32G : 32 G |
        | Monitor  | Maximum Resolution | 3440 x 1440 | 3440x1440 : 3440 x 1440   |
        | Monitor  | Refresh Rate       | 100 Hz      | 100Hz : 100 Hz            |
        | Keyboard | Brand              | Logitech    | Logitech                  |
```

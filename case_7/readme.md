# Case #7 is completed

### The pagination for test cases has been added.

Now we can walk around website pages and execute test cases on the single page as several pages and all pages

All this steps were implemented in "filters.feature" file.

The steps were added:

```gherkin
When Turn to page "<page_number>"
# page_number can be a number, "next", "previous" or "random" page

When Do on pages from "<start_page>" to "<end_page>" next steps
# Execute steps on pages from start_page to end_page or vice versa
# Steps should be in the table below like this:
| Steps                                          |
| Then "<KEYWORDS>" should be in the items title |

And For all pages
# Execute steps on all pages
# Steps should be in the table below like this:
| Steps                                          |
| Then "<KEYWORDS>" should be in the items title |

```

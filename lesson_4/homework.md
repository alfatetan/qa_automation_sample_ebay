### Lesson 4

## Homework tasks:

- [x] eBay item filters - follow the class on xpath grouping for widgets
      Xpath brainteasers:
- [x] register with any mail at http://www.old.practicalsqa.net/
      go to Brainteasers from top menu
      NOTE: "" (double quotes not needed there)

## Results

### Code practice

I combined the two tasks into one to test several filters in cell phone classification.
In my code here (Lesson #4) I left just search results checking.

Oddly enough, the test revealed a few bugs in the actual performance of the eBay website.

## In results.txt you can see the test results. I

http://www.old.practicalsqa.net/

Practical SQA paths are:

### Beginning

- [x] Nested Selectors

```py
#Find the list items for all the irritating things in September.
//div[@class="september"]/div[@class="irritating"]/ul/li
```

- [x] Behinning Conditionals

```py
# Get the link for all cars that priced $25,000
//div[./span[@class="price" and contains(text(), "$25,000")]]/a
```

- [x] Behinning Conditionals #2

```py
# Get the link for all Fords with the year greater then 1950
//div[./span[@class="make" and text()="Ford"] and ./span[@class="year" and text() > 1950]]/a
```

- [x] Behinning Conditionals #3

```py
# Get the link for all Fords made in 1958.
//div[./span[@class="make" and contains(text(), "Ford")] and ./span[@class="year" and text()="1958"]]/a
```

- [x] Find number of patient

```py
# Find family name of the patient born on 17 Dec 1955?
//patient[.//birthtime[@value="19551217"]]/name/family
```

- [x] Find the rate

```py
# Find the rate where loantype is "30-Year Fixed Rate" and subtype is "B"
//rate[./subtype[text()="B"] and ./loantype[text()="30-Year Fixed Rate"]]
```

- [x] Find the color

```py
# Get the value of mathcolor where colorvalue is 10
//color[./colorvalue[text()="10"]]/mathcolor/text()
```

### Advanced

- [x] Querying Subchildren

```py
# Find the values of id if their sub-node meta contains 123456
//produit[.//meta[@value='123456']]/@id
```

- [x] :question: Finding By Number of Elements

```py
# Find the h1s for every div with three list elements in it
//div/div[.//li[3]]/h1

# Perhaps, I solved this problem incorrect. I googled and found a XPath function as "count()" returns a count of elements. However I didn't find the way to use it. I solved a problem use more devious way. My logic were: if the list don't have 3rd element it wouldn't show up. Could you say is it correct or not? Or I should find a way to use the "count()" function?
```

- [x] Finding Sibling Elements

```py
# Q. I am positioned in the node[@id='1']. I need an Xpath to match all the elements until the next not empty node (here node[@id='2'])
//node[preceding-sibling::node[@id="1"] and following-sibling::node[@id="2"]]
```

- [x] Matching Text

```py
# Find the XPath for "match text"
//a[contains(text(), "match text")]/text()
```

- [x] Find percentage

```py
# For year 2016 return the Percentage
//percentage[preceding-sibling::*[contains(text(), "2016")]]
```
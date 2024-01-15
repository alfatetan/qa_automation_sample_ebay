# Homework Lesson 1. XPaths

[Click here to return to README.MD file](../README.md)

<i>I tried to use different ways to achieve elements. E.g., most Amazon elements have IDs properties. Sometimes, I avoid it, especially because wanted more practice.</i>

All XPaths were written in ECMAScript 6 (JavaScript) format.

## [eBay](https://www.ebay.com/)

```javascript
// common banner area
$x(
  `//div[contains(@class, 'vl-banner-color-block')]/div[contains(@class, 'content')]`
)[0];

//third element between shoes under the carousel
$x(`//div[contains(@class, 'carousel__viewport')]/ul/li`)[6];

// footer, left column, menu point "Registration"
$x(
  `//div[@id = 'gf-BIG']/table/tbody/tr/td/ul/li/a[contains(text(), 'Registration')]`
);
```

## [Amazon](https://www.amazon.com/)

```javascript
// logo
$x(`//div[@id='nav-logo']`);

// cart (I can achieve it easily but I try alternative way)
$x(
  `//div[contains(@class, 'layoutToolbarPadding')]/a[contains(@href, 'cart')]`
);

// search input field (without id attribute)
$x(`//input[contains(@aria-label, 'Search Amazon')]`);

// clickable footer zone "Back to Top"
$x(`//div[contains(@class, 'FooterBack')]`);
```

## [iHerb](https://www.iherb.com/)

```javascript
// top left corner "eGift Cards" link
$x(`//a[contains(text(), 'eGift')]`);

// cart icon (top right corner)
$x(`//div[@class='iherb-header-cart']`);

// input field "Trending Now"
$x(
  `//b[contains(text(), 'Trending now')]/../div[contains(@class, 'region-filter')]/input[@data-value='country']`
);
```

### Please, evaluate the quality of my homework assignment.

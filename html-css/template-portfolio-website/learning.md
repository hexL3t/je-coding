# Introduction to CSS

## What is CSS?
CSS is the acronym for Cascading Style Sheets.
It is used to style HTML elements
Separates content (HTML) from presentation (CSS)

## Why use CSS?
* Consistency
* Maintainability
* Efficiency
* Responsiveness


## Linking a CSS File
* Create a new CSS file (e.g., style.css)
* Link the CSS file to your HTML document using the <link> tag:
HTML
``` html
<link rel="stylesheet" href="style.css">
```

## Basic CSS Syntax
Structure of a CSS rule:
 
``` css 
Selector { 
    property: value; 
}
```
Example:
``` css
body {
    font-family: Arial, sans-serif;
    color: #333;
}
```

## Common properties:
* font-family, font-size, font-weight, color
* background-color, border, margin, padding

Example Use:
``` css
h1 {
    font-family: Arial, sans-serif;
    font-size: 16px;
    font-weight: bold;
    color: orange;
}
div {
    background-color: orange;
    border: 1px solid black;
    padding: 0;
    margin: 0;
}
```

## Understanding CSS Selectors
CSS selectors are the patterns you use to target specific HTML elements to which you want to apply styles. They are the first part of a CSS rule.

### Basic Selectors
#### Element Selectors
* Target all elements of a specific type.
* Syntax: element_name

Example:
``` css
p {
    color: blue;
}
```
This will apply blue color to all <p> elements in your HTML.

#### Class Selectors
* Target elements with a specific class attribute.
* Syntax: .class_name

Example:
``` css
.highlight {
    background-color: yellow;
}
```
You can apply this style to any element with the class "highlight":
``` html
<p class="highlight">This paragraph is highlighted.</p>
<div class="highlight">This div is also highlighted.</div>
```

#### ID Selectors
* Target a single element with a unique ID attribute.
* yntax: #id_name

Example:
``` css
#header {
    background-color: red;
}
```
This style will be applied only to the element with the ID "header":
``` html
<header id="header">This is the header</header>
```

### Combining Selectors
You can combine multiple selectors to create more specific rules.

#### Group Selectors
* Apply the same styles to multiple elements.
* Syntax: selector1, selector2, selector3

Example:
``` css
h1, h2, h3 {
    font-family: Arial, sans-serif;
}
```

#### Descendant Combinator
* Selects all elements that are descendants of another element.
* Syntax: parent element child element
Example:
``` css
div p {
    color: green;
}
```
This will apply green color to all <p> elements that are inside a <div>.

#### Child Combinator
* Selects all elements that are direct children of another element.
* Syntax: parent element > child element
Example:
``` css
ul > li {
    list-style-type: square;
}
```
This will apply square list style to all <li> elements that are direct children of a <ul>.

#### Attribute Selectors
* Select elements based on their attributes.
* Syntax: element[attribute]
Example:
``` css
a[href^="https://"] {
    color: blue;
}
```
This will apply blue color to all <a> elements with href attribute starting with "https://".

### Pseudo-classes and Pseudo-elements
These are special selectors that allow you to style elements based on their state or to style specific parts of an element.

* ```Pseudo-classes:``` Target elements based on their state (e.g., :hover, :active, :focus).
* ```Pseudo-elements:``` Style specific parts of an element (e.g., ::before, ::after).

## The CSS Box Model
The CSS box model is a fundamental concept in web design, representing every HTML element as a rectangular box composed of four main parts:

* ```Content:``` This is the actual content of the element, such as text, images, or other elements. Its dimensions are determined by the width and height properties.
* ```Padding:``` This is the clear space around the content, inside the border. It's defined using the padding property.
* ```Border:``` This is the line drawn around the element, encompassing both content and padding. It's defined using the border property.
* ```Margin:``` This is the clear space outside the border, separating the element from other elements. It's defined using the margin property.

### Box-Sizing Property

To manage the total width of an element, the ```box-sizing``` property comes in handy. It determines how the ```width``` and ```height``` properties are calculated.

* ```box-sizing: content-box;``` (default): The width and height properties apply only to the content box. Padding and border are added to the total width.
* ```box-sizing: border-box;``` The width and height properties include padding and border, so the content area is smaller.
Practical Example
``` css
.box {
  width: 200px;
  height: 150px;
  border: 5px solid black;
  padding: 10px;
  margin: 20px;
}
```
In this example:
* The content area will be 180px wide and 130px high (200px - 25px border - 210px padding).
* The total width of the element will be 220px (200px + 25px border + 210px padding).
* The element will be separated from other elements by 20px on all sides due to the margin.

## Basic Layout with Margin and Padding
* Use margin and padding to create spacing between elements

Example:
```CSS
.container {
    margin: 20px;
    padding: 10px;
}
```

## Introduction to Flexbox
### What is flexbox?
Flexbox, or Flexible Box, is a one-dimensional layout model designed to arrange items within a container. It provides a powerful and efficient way to create responsive and dynamic layouts.

Key Components:
* Flex Container: The parent element that holds the flex items.
* Flex Items: The child elements within the flex container.
* Basic Flexbox Properties

### On the Container
* ```display:``` flex; Turns an element into a flex container.
* ```flex-direction:``` Defines the direction of the flex items.
* ```row:``` Default, items are laid out horizontally.
* ```row-reverse:``` Items are laid out horizontally in reverse order.
* ```column:``` Items are laid out vertically.
* ```column-reverse:``` Items are laid out vertically in reverse order.
* ```flex-wrap:``` Determines if flex items should wrap to the next line.
* ```nowrap:``` Default, no wrapping.
* ```wrap:``` Items wrap to the next line if there's no space.
* ```wrap-reverse:``` Items wrap to the next line in reverse order.
* ```justify-content:``` Aligns flex items along the main axis.
* ```flex-start:``` Items are aligned to the start of the container.
* ```flex-end:``` Items are aligned to the end of the container.
* ```center:``` Items are centered within the container.
* ```space-between:``` Items are evenly distributed with space between them.   
* ```space-around:``` Items are evenly distributed with space around them.   
* ```space-evenly:``` Items are evenly distributed with equal space between them and the container edges.
* ```align-items:``` Aligns flex items along the cross axis.
* ```flex-start:``` Items are aligned to the start of the container.
* ```flex-end:``` Items are aligned to the end of the container.
* ```center:``` Items are centered within the container.   
* ```stretch:``` Items are stretched to fill the container.
* ```baseline:``` Items are aligned based on their baseline.

### On the Items
* ```order:``` Defines the order of flex items.
* ```flex-grow:``` Defines how much the item should grow relative to the others.
* ```flex-shrink:``` Defines how much the item should shrink relative to the others.
* ```flex-basis:``` Defines the initial size of the item before distribution.
* ```align-self:``` Overrides the align-items property for individual items.

### Example
#### HTML
```HTML
<div class="container">
  <div class="item">Item 1</div>
  <div class="item">Item 2</div>
  <div class="item">Item 3</div>
</div>
```
#### CSS
```CSS
.container {
  display: flex;
  justify-content: space-between;   
}
```

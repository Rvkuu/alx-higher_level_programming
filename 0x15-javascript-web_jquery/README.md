What Is JavaScript
Welcome to the MDN beginner's JavaScript course! In this article we will look at JavaScript from a high level, answering questions such as "What is it?" and "What can you do with it?", and making sure you are comfortable with JavaScript's purpose.

Prerequisites:	Basic computer literacy, a basic understanding of HTML and CSS.
Objective:	To gain familiarity with what JavaScript is, what it can do, and how it fits into a website.

A high-level definition
JavaScript is a scripting or programming language that allows you to implement complex features on web pages — every time a web page does more than just sit there and display static information for you to look at — displaying timely content updates, interactive maps, animated 2D/3D graphics, scrolling video jukeboxes, etc. — you can bet that JavaScript is probably involved. It is the third layer of the layer cake of standard web technologies, two of which (HTML and CSS) we have covered in much more detail in other parts of the Learning Area.
HTML is the markup language that we use to structure and give meaning to our web content, for example defining paragraphs, headings, and data tables, or embedding images and videos in the page.
CSS is a language of style rules that we use to apply styling to our HTML content, for example setting background colors and fonts, and laying out our content in multiple columns.
JavaScript is a scripting language that enables you to create dynamically updating content, control multimedia, animate images, and pretty much everything else. (Okay, not everything, but it is amazing what you can achieve with a few lines of JavaScript code.)
The three layers build on top of one another nicely.

What is JavaScript doing on your page?
Here we'll actually start looking at some code, and while doing so, explore what actually happens when you run some JavaScript in your page.

Let's briefly recap the story of what happens when you load a web page in a browser (first talked about in our How CSS works article). When you load a web page in your browser, you are running your code (the HTML, CSS, and JavaScript) inside an execution environment (the browser tab). This is like a factory that takes in raw materials (the code) and outputs a product (the web page).
A very common use of JavaScript is to dynamically modify HTML and CSS to update a user interface, via the Document Object Model API (as mentioned above). Note that the code in your web documents is generally loaded and executed in the order it appears on the page. Errors may occur if JavaScript is loaded and run before the HTML and CSS that it is intended to modify. You will learn ways around this later in the article, in the Script loading strategies section.

Getting and setting CSS classes
Just like it's very easy to manipulate content and attributes of elements, as we saw in the previous chapters, it's equally easy to manipulate the CSS of elements. jQuery gives you easy access to changing both the style attribute, which you manipulate using the css() method, as well as the class(es) of an element, where several different methods lets you modify it.

Let's start by looking into changing the class attribute. The class attribute takes one or several class names, which may or may not refer to a CSS class defined in your stylesheet. Usually it does, but you may from time to time add class names to your elements simply to be able to reach them easily from jQuery, since jQuery has excellent support for selecting elements based on their class name(s).

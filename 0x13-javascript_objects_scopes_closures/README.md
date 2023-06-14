In this article, we'll look at fundamental JavaScript object syntax, and revisit some JavaScript features that we've already seen earlier in the course, reiterating the fact that many of the features you've already dealt with are objects.

Prerequisites:	Basic computer literacy, a basic understanding of HTML and CSS, familiarity with JavaScript basics (see First steps and Building blocks).
Objective:	To understand the basics of working with objects in JavaScript: creating objects, accessing and modifying object properties, and using constructors.
Object basics
An object is a collection of related data and/or functionality. These usually consist of several variables and functions (which are called properties and methods when they are inside objects). Let's work through an example to understand what they look like.

To begin with, make a local copy of our oojs.html file. This contains very little — a <script> element for us to write our source code into. We'll use this as a basis for exploring basic object syntax. While working with this example you should have your developer tools JavaScript console open and ready to type in some commands.

As with many things in JavaScript, creating an object often begins with defining and initializing a variable. Try entering the following line below the JavaScript code that's already in your file, then saving and refreshing

Classes and constructors
You can declare a class using the class keyword. Here's a class declaration for our Person from the previous article:

class Person {
  name;

  constructor(name) {
    this.name = name;
  }

  introduceSelf() {
    console.log(`Hi! I'm ${this.name}`);
  }
}
Copy to Clipboard
This declares a class called Person, with:

a name property.
a constructor that takes a name parameter that is used to initialize the new object's name property
an introduceSelf() method that can refer to the object's properties using this.
The name; declaration is optional: you could omit it, and the line this.name = name; in the constructor will create the name property before initializing it. However, listing properties explicitly in the class declaration might make it easier for people reading your code to see which properties are part of this class.

You could also initialize the property to a default value when you declare it, with a line like name = '';.

The constructor is defined using the constructor keyword. Just like a constructor outside a class definition, it will:

create a new object
bind this to the new object, so you can refer to this in your constructor code
run the code in the constructor
return the new object.
Given the class declaration code above, you can create and use a new Person instance like this:

const giles = new Person("Giles");

giles.introduceSelf(); // Hi! I'm Giles
Copy to Clipboard
Note that we call the constructor using the name of the class, Person in this example.

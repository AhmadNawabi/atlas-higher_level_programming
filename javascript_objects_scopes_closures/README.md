# JavaScript - Objects, Scopes, and Closures

Welcome to the JavaScript - Objects, Scopes, and Closures repository! This repository serves as a comprehensive guide to understanding and mastering these essential concepts in JavaScript. Whether you're a beginner looking to solidify your understanding or an experienced developer seeking to deepen your knowledge, you'll find valuable insights and practical examples here.

## Table of Contents

1. [Objects](#objects)
2. [Scopes](#scopes)
3. [Closures](#closures)

## Objects

JavaScript is an object-oriented programming language, and objects play a fundamental role in it. Objects are collections of key-value pairs, allowing you to represent complex data structures. Here's a simple example of creating and using objects in JavaScript:

```javascript
// Creating an object
let person = {
    name: 'John Doe',
    age: 30,
    occupation: 'Developer'
};

// Accessing object properties
console.log(person.name); // Output: John Doe
console.log(person.age); // Output: 30
console.log(person.occupation); // Output: Developer

// Modifying object properties
person.age = 35;
console.log(person.age); // Output: 35

// Adding new properties
person.location = 'New York';
console.log(person.location); // Output: New York


# JavaScript - Scopes

 This repository serves as a comprehensive guide to understanding scopes in JavaScript. Scopes are crucial for writing efficient and maintainable JavaScript code. JavaScript has two main types of scope: global scope and local scope.

## Table of Contents

1. [Scopes](#scopes)

## Scopes

Understanding scopes is crucial for writing efficient and maintainable JavaScript code. JavaScript has two main types of scope: global scope and local scope. Here's a basic example demonstrating scope in JavaScript:

```javascript
// Global scope
let globalVariable = 'I am a global variable';

function myFunction() {
    // Local scope
    let localVariable = 'I am a local variable';
    console.log(globalVariable); // Output: I am a global variable
    console.log(localVariable); // Output: I am a local variable
}

myFunction();

console.log(globalVariable); // Output: I am a global variable
console.log(localVariable); // Output: Uncaught ReferenceError: localVariable is not defined


In the example above, globalVariable is accessible both inside and outside the function myFunction, while localVariable is only accessible within the function where it's defined.



# JavaScript - Closures

Welcome to the JavaScript - Closures repository! This repository serves as a comprehensive guide to understanding closures in JavaScript. Closures are powerful and often misunderstood concepts in JavaScript. A closure is created when a function is defined inside another function and has access to the outer function's variables.

## Table of Contents

1. [Closures](#closures)

## Closures

Closures are powerful and often misunderstood concepts in JavaScript. A closure is created when a function is defined inside another function and has access to the outer function's variables. Here's an example demonstrating closures:

```javascript
function outerFunction() {
    let outerVariable = 'I am from outer function';
    
    function innerFunction() {
        console.log(outerVariable); // Inner function has access to outerVariable
    }
    
    return innerFunction;
}

let closureExample = outerFunction();
closureExample(); // Output: I am from outer function


In this example, innerFunction forms a closure over the outerVariable, even after outerFunction has finished executing. This allows innerFunction to access outerVariable when it's called later.

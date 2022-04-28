Think of scope as variable access. 

var 
- function scoped or global scoped
    - if not declared in a function, the variable is globally scoped

const, let 
- block scoped
    - a block is anything between {}, functions are also blocks, for loops also create a separate block
    
It is also possible to declare variables without the var, const, and let keywords. Those variables will either find the closest variable with the same name and reassign the value, or create a globally scoped variable.

```
function sayHello() {
    let greeting = "Hello";
    console.log(greeting);
}
console.log(greeting); // error, since let is scoped to the function
```

```
var greeting = "Hello";
function sayHello() {
    console.log(greeting);
}
console.log(greeting); // "Hello", since var is globally scoped
```

```
if (true) {
    var greeting = "Bonjour";
}
console.log(greeting); // "Bonjour", since greeting is declared with var and not within a function so it is globally scoped
```

```
if (true) {
    let greeting = "Bonjour";
}
console.log(greeting); // error since greeting is declared with let so it is scoped to the if statement
```
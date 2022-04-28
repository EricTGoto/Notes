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

<b>Closure</b>

- a closure is a function that remembers its outer variables and can access them
- in JS, a closure is created every time a function is created
- a closure is the combination of a function and the lexical environment within which that function was declared 

Example:
```
function makeFunc() {
    var name = "Hello";
    function displayName() {
        console.log(name);
    }
    return displayName;
}
var myFunc = makeFunc();
myFunc();
```
displayName is a closure and it closes over the variable name. This code still works because javascript functions form closures. The displayName function has access to name.

Closures allow the concept of private variables and functions in Javascript. The concept of private variables and functions is closely tied to the factory function design pattern.

```
const FactoryFunction = string => {
  const capitalizeString = () => string.toUpperCase();
  const printString = () => console.log(`----${capitalizeString()}----`);
  return { printString };
};

const taco = FactoryFunction('taco');

printString(); // ERROR!!
capitalizeString(); // ERROR!!
taco.capitalizeString(); // ERROR!!
taco.printString(); // this prints "----TACO----"
```
FactoryFunction returns a function printString which is accessible publically.  Because of function scope, the first two function calls fail. taco.capitalizeString returns an error also because of functional scoping. since capitalizeString is not accessible, it can be thought of as private. taco.printString() works as FactoryFunction is a function factory that creates and returns the printString() function, which is a closure that contains capitalizeString within its environment.
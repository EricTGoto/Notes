# SOLID Principles

SOLID is an acronym for 5 OOP design principles:
1. Single Responsibility Principle
2. Open/Closed Principle
3. Liskov Substitution Principle
4. Interface Segregation Principle
5. Dependency Inversion Principle

<h3>Single Responsibility Principle</h3>

- an object should only have responsibility over one part of a program's functionality
- doesn't mean that an object can only do one thing, it can do multiple things, but together it should only represent one cohesive function

Coupling:
- coupling is how much objects rely on another object. 
    - tightly coupled objects rely on each other heavily and a change in one object means that the other object will also need to be changed. 
        - tightly coupled objects make it harder to create scalable and maintable applications as modules cannot be swapped in and out easily
        - reusability is also reduced
    - loosely coupled objects don't have much dependence on each other, if at all
        - examples: Pub/Sub, observer pattern
<h3>Open-Closed Principle</h3>

- modules should be open to extension, but closed to modification
- if someone wants to extend the module's behaviour, they don't need to modify the existing code

<h3>Liskov Substitution Principle</h3>

- concept where a subclass must obey all rules of the class it inherits or extends
- for example, one may make Square inherit from a Rectangle, but a Rectangle would have the setWidth and setHeight methods which don't make sense for a Square to have as setting the width would set the height and vice versa

<h3>Interface Segregation</h3>

- client shouldn't need to implement interfaces that they do not use

<h3>Dependency Inversion Principle</h3>

- make it so high level code depends on abstractions and are not dependent on specific implementations of items
- for example, a connection string parameter for a class that does operations on a database can be implemented with a specific connection string, but that would break the dependency inversion principle and the open closed principle as if you wanted to use a different database, you would not be able to use it without changing the code. so you make the connection string parameter generic
- you don't want to hand over control to another function
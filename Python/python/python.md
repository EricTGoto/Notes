Python Notes

Classes

- named in camel case
- example declaration:
    class Car:
        pass
- constructor is def __init__(self):
- create methods by defining functions within a class
- is operator used to checking if two references refer to the same object, while == will tell you if contents are the same
- goal of OOP is to include any functionality which handles objects of a certain type in the class definition as methods, i.e. don't create functions that handle objects, create methods
- __str__ method lets you print out objects with a self defined string
- declare a variable with the self parameter name and it becomes an attribute of the object and will exist for as long as the object exists
- if a method or attribute does not exist, None will be returned, so it is good to check for None before trying to access any attributes or methods of return values
- class variables aka static variables are variables that are shared amongst all instances of a class and are defined at the top of the class without the self prefix
- class method/static methods is a method not attached to any single instance of a class, can be called without creating any instances of the class, use the @classmethod annotation and the first parameter must be cls

OOP

- Client: program which uses a class, instances of a class
- methods dedicated to accessing and changin attributes are called getters and setters, use @property decorator in python

Encapsulation
- if data within an object is only used through the methods within the object, the internal integrity is guaranteed. this is called encapsulation
- in practice, integrity means that the values of the object's attributes are always acceptable, e.g. an object representing a date should never have 13 as the value of the month
- we can do this by making it so that only the class itself can modify parameters, by using private attributes
- private attributes are created by adding two underscores __ to the beginning of the attribute name
- clients cannot access private attributes directly, if they try it will return an error
- private attributes usually come with getter and setter methods for controlling access to them, while private methods are intended for **internal** use
- a method should be hidden whenever the client has no need to directly access it

Default values of parameters:
- if a parameter has a default value, it is optional when calling a function
``` def something(a, b, c = 0) ```
- the parameter c is optional and you can call something by only including parameters a and b
- the default value of a parameter should not be set to a mutable data structure like a list or you will encounter problems as it will reuse the reference
- instead use the constructor to initialize the variable (see example.py)

Inheritance:

- a class can inherit the traits of another class
- the syntax for inheriting is to simply add the base class name in parentheses on the class declaration line
``` 
class Animal:
    pass
    
class Dog(Animal):
    pass
```
- a method with the same name in the derived class overrides the original method, this is called overriding
- any trait in the base class can be accessed from the derived class with the function super()
- private attributes/methods are inaccessible to clients which includes any subclasses. There is a convention to protect a trait from a client but make it accessible to subclasses by using a single underscore to make it a protected trait

Operator Overloading

- python includes special methods that allow classes to work with standard arithmetic and comparison operators
- for example the operator >'s functionality can be defined with \__gt__
```
class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__name} (price {self.__price})"

    @property
    def price(self):
        return self.__price

    def __gt__(self, another_product):
        return self.price > another_product.price
```

```
orange = Product("Orange", 2.90)
apple = Product("Apple", 3.95)

if orange > apple:
    print("Orange is greater")
else:
    print("Apple is greater")
```
- other methods are lt, eq, ne, le.. etc

- \__repr__ returns the technical representation of an object, often implemented so that it returns the code which can be executed to return an object with identical contents to the current object

```
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f"Person({repr(self.name)}, {self.age})"
```

```
person1 = Person("Anna", 25)
person2 = Person("Peter", 99)
print(person1)
print(person2)
```
Output is:
```
Person('Anna', 25)
Person('Peter', 99)
```

Iterators
- it is possible to make your own classes iterable
- to make a class iterable you must implement the iterator methods \__iter__ and \__next__
- the iteration method usually just initializes an iteration variable
- the next method returns the next item or returns a StopIteration event once all items have been traversed

List Comprehensions

- Syntax: [<expression> for <item> in <list>]
- e.g. strings = [str(number) for number in numbers] where numbers is a list of numbers

List comprehensions also allow for a condition: [<expression> for <item> in <list> if <boolean expression>]
If you want an else in a comprehension, move the if to the front: [<expression 1> if <boolean expression> else <expression 2> for <item> in <list> ]

Dictionary Comprehensions:
{<key expression>: <value expression> for <item> in <series>}

Custom Sorting:
- by default, sorts will sort by natural order (ascending order)
- if you want to change this, use the optional argument key, which is a function that is used for key comparison

Regex:

|: pipe character, acts as an or

[ ]: square brackets, used to signify groups of accepted chracters

e.g. [aeio] matches all strings which contain any of the characters a,e,i,o

e.g. [0-6] matches all strings which contain a digit from 0 to 6

[0-68a-d] matches all strings which contain a digit from 0 to 6 or an 8 or a letter from a-d

two sets of brackets let you match two consecutive characters

(): round brackets to group parts of expression

-: dash, for ranges of characters

.: match any single character

^: character following must be at beginning of string

$: character preceding must be at the end of string

Repeated matches:
a part of an expression can be repeated with the following operators (works on part of expression preceding operator):
- * repeats for any number of times, including zero
- + repeats for any number of times, but at least once
- {m} repeats for exactly m times

e.g. ba+b would match bab baaaaab, but not bb

ba*b would match bab baaaab and bb
ba{1}b would only match bab


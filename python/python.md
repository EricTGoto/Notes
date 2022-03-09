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
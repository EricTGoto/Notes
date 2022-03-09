class Person:
    species = "Homo Sapiens" #this is a class/static variable

    # constructor, the person class must be made with the parameters name and year of birth
    def __init__(self, name: str, year_of_birth: int, name_of_children=None):
        self.name = name
        self.year_of_birth = year_of_birth
        self.__money = 500 # this value is private and clients cannot access it directly
        self.__is_alive = True

        if name_of_children is None:
            self.name_of_children = []
        else:
            self.name_of_children = name_of_children
            

    # changes the print command to return a string instead of the object memory reference
    def __str__(self) -> str:
        return f'This is {self.name}!'

    # method that compares ages of two people
    # when type hinting a parameter that is of the same type as the class itself, the type must be in quotation marks
    def older_than(self, another: "Person"):
        return self.year_of_birth < another.year_of_birth

    # use the @property decorator to create a setter
    # the client can use xxx.money to access the money attribute now
    # the @property decorator must be introduced before the setter method as it defines the name of the attribute that it will reveal to the client
    @property
    def money(self):
        return self.__money
    
    @money.setter
    def money(self, money):
        if money >= 0:
            self.__money = money
    
    @classmethod
    def is_alive(cls, person: "Person"):
        return person.__is_alive


if __name__ == "__main__":
    bob = Person("Bob", 2000)
    print(bob) #prints This is Bob!

    #bob.__money will return an error because the attribute is private
    # this uses the getter so it will not return an error
    print(bob.money)
    print(Person.is_alive(bob)) # utilizing the class method to check if a person is alive
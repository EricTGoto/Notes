# list comprehension syntax
# [<expression> for <item> in <list>]

numbers = [1, 2, 3, 4, 5, 7]
strings = [str(number) for number in numbers]
print(strings)

# list comprehensions work on functions you created as well
def multiply_by_10(number : int):
    return number * 10

multiplied_by_10 = [multiply_by_10(number) for number in numbers]
print(multiplied_by_10)
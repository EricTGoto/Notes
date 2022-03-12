import re
strings = ["baab", "bab", "baaaaaab", "bb"]
expression1 = "ba{1}b" # prints out only bab
expression2 = "ba+b" # prints out everything but bb
expression3 = "ba*b" # prints everything

for string in strings:
    if re.search(expression3, string): print(string)


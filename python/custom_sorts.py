products = [("banana", 5.95), ("apple", 3.95), ("orange", 4.50), ("watermelon", 4.95)]

# sort will sort by the 0th index (the strings), but if we want to specify a different index we use the key parameter

def sort_by_1st_index(item: tuple):
    return item[1]

sorted_list = sorted(products, key = sort_by_1st_index)

print(sorted_list)
# returns: [('apple', 3.95), ('orange', 4.5), ('watermelon', 4.95), ('banana', 5.95)]
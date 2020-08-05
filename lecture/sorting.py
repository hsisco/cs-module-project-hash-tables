# If you iterate across, or print a hash table, will the items be in the order you add them?
# No. Sets and objects are not ordered, unlike lists/arrays

# Python dictionaries DO preserve order

# SORTING
my_list = [99,45,12,67,23,5]
# sorted, list.sort() - mixture of sorting algorithms

# Basically hash table with methods added
my_dict = {"foo": 11,"bar":42,"qux":99}

# It doesn't make sense to sort a hash table
# sort a list based on the dictionary

# Lambda Functions are much like anonymous functions in JS
# JS: (x) => x[1]

# sorted takes key=lambda, uses what the anonymous functnion returns to sort

# use lambda function to sort by value
# sorted(my_items, key=lambda x: x[1])

my_dict_items = list(my_dict.items())
# sort by value
my_dict_items.sort(key=lambda x: x[1])
# sort by value, decending order
my_dict_items.sort(key=lambda x: x[1], reverse=True)
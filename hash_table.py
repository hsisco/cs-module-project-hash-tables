# Build a data structure that will let us search for info really fast
## Using an array and a function
#  'get' and search are the same thing
## Given a list of a trillion elements, find a string O(1)
## Hack: turn a string into an index
## That way we can jump there immediately

# Building a dictionary, {}, from scratch

# To turn a string into an index, we built a hash function
### The hash func takes a string, turns it into a  number, scrambles the number, and gives it back to us

# WE make sure the number we get back works with our list --> index
# Use our new index!

# EXAMPLE
# Use key-value pair: "hello", "hello world"
## 1: hash "hello"
## 2: make HASH work with list - turn into index
## 3: PUT value in that index!

# Look it up!
## 1: hash "hello"
## 2: make RESULT work with list - turn into index
## 3: GO to that index

# set() = hash table where the key & value are the same

# Note: need to know the string we used!
# NEVER APPEND!!

# new_list[0] = "hello world"
# hello --> 0
# hash(world) --> 4

my_list = ['hi', 'how', 'are', 'you', 'hello', 'world']

# Time complexity of search? O(n)
# my_list.contains() --> still a for loop, so still O(n) (just easier to write)

# What if we had a function to tell us the index of 'hello' in O(1)?

# HASHING FUNCTION: hashes and returns a hash; Deterministic
# def my_func(string_to_search_for):
#     return index_of_string

# my_index = my_func("hello") # 4
# my_list[my_index]           # hello

# Naive:
# Most take a string
# Return an integer
# Operates on the bytes of the string
## byte: an integer 0-255 via binary (00000000 - 11111111)
#                                         0         255

# def my_hash(string):
#     for character in string:
#         print(character)

# my_hash("hello")

# my_bytes = {'a': 65, 'b': 66}

# for thing in "hello".encode():
#     print(thing)                # 104, 101, 108, 108, 111

# ASCII maps letters to numbers: Latin alphabet, Arabic numerals
# UTF-8 like ASCII on steroids, mapping letters to numbers

# Unicode Transformation Format-8
# Next, we want to transform the bytes into a random-looking number
# We want different strings to come back with different numbers as spread out as possible over our array
def my_hash(string):
    string_bytes = string.encode()
    total = 0
    for characters in string_bytes:
        total += characters

    return total

print(my_hash("hello"))
print(my_hash("world"))

#  What would happen if we got back the same number/index for different words? (palendrome, anagram)
# add, dad
## COLLISION!

# How to use the number we return (the 'hash') to get an index in a list?

# my_list[hello_hash]             # IndexError: list index out of range

new_list = [None] * 8

# modulo:
# 9 % 8   # 1
# 10 % 8  # 2
# 16 % 8  # 0
# 17 % 8  # 1


# Put "howdy world" in new_List at index "world"
## 1: put "world" through the hashing function
hello_hash = my_hash("hello")
## 2: modulo that result with the length of our list
hello_index = hello_hash % len(new_list)
## 3: use that modulo - index -  with our list
new_list[hello_index] = "hello world"

# PUT:
hashed_world = my_hash("world")
world_index = hashed_world % len(new_list)
new_list[world_index] = "howdy world"
print(new_list)

# key-value store: Python: dictionary, JS: object, Swift: dictionary

# Get/Search for "howdy world", given "world" or "hello"
## 1: get the hash
hashed_string = my_hash("hello")
## 2: take hash modulo length of our array
our_index = hashed_string % len(new_list)
## 3: use that index to access the value stored there
print(new_list[our_index])

# Time complexity of Get and Put:
## Depends whether you measure by the string we put in, or the list we use as a table/storage
## String/Key: O(n) aka Linear, because we iterate over the string
## List: O(1) aka Constant
## Hashtables: O(1)


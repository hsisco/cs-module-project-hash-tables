# FIBONACCI SEQUENCE
# the next number is the sum of the previous two
# 0,1,1,2,3,5,8,13,21,34,55,89,...

# base case
# progress toward the base case
# call itself (recursion)

# def fib(n):                     # O(2^n)
#     # base case                 # O(#_times_calls_self ^ n) --> horrendous!
#     if n <= 1:
#         return n
#     return     fib(n-1) + fib(n-2)
    
# print(fib(40))    # Takes about 30 sec to get answer: 102334155

# We'd have to wait until the heat-death of the universe for an answer if we enter a large enough number

# MEMOIZATION
# base case
# progress toward the base case
# memoize in a cache
# call itself (recursion)
cache = {}

def fib(n):                     
    if n <= 1:
        return n
    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]
    
print(fib(40))  # Immediately returns 102334155
print(fib(400))

# Memoization
# Dynamic programming
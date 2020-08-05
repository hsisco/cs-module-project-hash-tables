# Resizing an array is linear (O(n^2))
# Option 1: Pre-allocating
my_arr = [None] * 100000000000

# Option 2: Pre-populate your cache
import math

def inverse_sqrt(num):
    return 1 / math.sqrt(num)

cache = {}

def populate_cache():
    for i in range(1, 1000):
        cache[i] = inverse_sqrt(i)

populate_cache()

print(inverse_sqrt(999))
print(cache[999])

# Lazy computation / lazily computed

# Hash table is:
# 1. hash function
# 2. backed by an array
# 3. some way to handle collisions (LL, or use open addressing)

# Dictionaries & objects =
# just hash tables with a few methods added (ie, .items(), .)
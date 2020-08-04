# 1: choose some big, random number, usually prime
# 2: loop over bytes of our string, and do something weird
# 3: return the weird result

new_list = [None] * 8

"""
DJB2 hash, 32-bit
"""
def djb2(s):
    hash_var = 5381
    string_bytes = s.encode()
    for b in string_bytes:
        hash_var = ((hash_var << 5) + hash_var) + b
    return hash_var

# def djb2(self, key):
#     hash_var = 5381
#     #                 string_bytes = s.encode()
#     for element in key:
#         hash_var = (hash_var * 33) + ord(element)
#     return hash_var

"""
FNV-1 Hash, 64-bit
"""
# def fnv(s):
#     FNV_offest_basis = 
#     FNV_prime = 

#     hash_var = FNV_offest_basis

#     string_bytes = s.encode()
#     total = 0
#     for b in string_bytes:
#         hash_var = hash_var * FNV_prime
#         hash_var = hash_var ^ b
#     return hash_var

def put(key,value):
    hashed_key = djb2(key)
    idx = hashed_key % len(new_list)
    new_list[idx] = value

put("hello", "hello world")
put("world", "howdy world")

def get(key):
    hashed_key: djb2(key)
    idx = hashed_key % len(new_list)
    value = new_list[idx]
    return value

print(get("hello"))
print(get("howdy"))

def delete(key):
    hashed_key = djb2(key)
    idx = hashed_key % len(new_list)
    new_list[idx] = None

# delete("hello")
put("barn", "moo cow")
print(get("barn"))
print(get("hello"))


# If 2 different keys hash to the same index, we have a COLLISION and the newest key overwrites the previous
## Solve with a linked list!
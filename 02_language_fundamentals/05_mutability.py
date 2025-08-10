"""Mutability determines whether an object can change after its creation.

Immutable objects (like strings or tuples) cannot be altered in place.
Mutable objects (like lists or dictionaries) can be modified.
"""

# Immutable example: attempting to modify a string raises an error
text = "hello"
try:
    text[0] = "H"
except TypeError as err:
    print("Strings are immutable:", err)

# Mutable example: lists allow item assignment
numbers = [1, 2, 3]
numbers[0] = 10
print("Lists are mutable:", numbers)

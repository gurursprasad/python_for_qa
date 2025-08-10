"""
In Python, data types define the nature of values a variable can hold.
Common built-in data types include:
    int      - whole numbers
    float    - numbers with a decimal point
    complex  - numbers with real and imaginary parts
    bool     - boolean values True or False
    str      - sequence of characters (text)
    list     - ordered, mutable collection of items
    tuple    - ordered, immutable collection of items
    set      - unordered collection of unique items
    dict     - key-value pairs
Below are simple examples of each data type.
"""

# Numeric Types
num_int = 10
num_float = 10.5
num_complex = 3 + 4j

print(type(num_int))
print(type(num_float))
print(type(num_complex))

# Boolean Type
is_valid = True

print(type(is_valid))

# String Type
message = "Hello, Python!"

print(type(message))

# Sequence Types
numbers_list = [1, 2, 3]
numbers_tuple = (1, 2, 3)

print(type(numbers_list))
print(type(numbers_tuple))

# Set Type
unique_numbers = {1, 2, 3}

print(type(unique_numbers))

# Mapping Type
data_dict = {"name": "Alice", "age": 30}

print(type(data_dict))

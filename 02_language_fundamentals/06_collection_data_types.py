"""Collection data types store multiple items in a single variable.

This example shows Python's common collections:
list, tuple, set, frozenset, dict, range, bytes, and bytearray.
"""

list_example = [1, 2, 3]
tuple_example = (1, 2, 3)
set_example = {1, 2, 3}
frozenset_example = frozenset({1, 2, 3})
dict_example = {"a": 1, "b": 2}
range_example = range(3)
bytes_example = b"ABC"
bytearray_example = bytearray(b"ABC")

print(type(list_example))
print(type(tuple_example))
print(type(set_example))
print(type(frozenset_example))
print(type(dict_example))
print(type(range_example))
print(type(bytes_example))
print(type(bytearray_example))

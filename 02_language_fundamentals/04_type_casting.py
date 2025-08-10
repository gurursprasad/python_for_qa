"""Type casting converts a value from one data type to another using built-in functions.

Examples:
    int("10") -> 10
    float("3.14") -> 3.14
    str(100) -> "100"

Use type casting to ensure values are in the expected format.
"""

# Implicit type casting (int + float becomes float)
result = 10 + 2.5
print(result, type(result))

# Explicit type casting
print(int("10"))
print(float("3.14"))
print(str(100))

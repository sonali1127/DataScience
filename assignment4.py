
# Create a tuple named my_tuple containing at least 
# five different elements (mix of integers, strings, and a float).
# Tuple Creation
my_tuple = (42, "hello", 3.14, "world", 100)
print("Tuple:", my_tuple)

# Accessing Elements
# Print the first and last element of my_tuple using indexing.
# Use negative indexing to access the second last element.

print("First Element:", my_tuple[0])
print("Last Element:", my_tuple[-1])
print("Second Last Element (Negative Indexing):", my_tuple[-2])

# Tuple Slicing
# Slice and print the first three elements of my_tuple.
# Slice and print the last two elements.

print("First Three Elements:", my_tuple[:3])
print("Last Two Elements:", my_tuple[-2:])

# Tuple Operations
# Concatenate my_tuple with another tuple and print the result.
# Repeat my_tuple twice and print the result.


another_tuple = ("extra", 999)
concatenated = my_tuple + another_tuple
print("Concatenated Tuple:", concatenated)

repeated = my_tuple * 2
print("Repeated Tuple:", repeated)

# Tuple Methods
# Find the index of a specific element in my_tuple and print it.
# Count the occurrences of a specific element in my_tuple and print it.

print("Index of 'hello':", my_tuple.index("hello"))
print("Count of 42:", my_tuple.count(42))

# Tuple Immutability
# Try changing one element in my_tuple and observe the result.
# Explain why tuples are immutable.

try:
    my_tuple[0] = 99  # This should raise an error
except TypeError as e:
    print("Error (Tuples are immutable):", e)

# Explanation
print("Explanation: Tuples are immutable, meaning their elements cannot be changed once assigned.")

# Tuple Packing and Unpacking
# Create a tuple with three elements and unpack them into individual variables.
# Print the unpacked values.

packed_tuple = ("Python", 101, 4.5)
lang, code, rating = packed_tuple
print("Unpacked Values:", lang, code, rating)

# Tuple Iteration
# Use a loop to iterate through my_tuple and print each element.

print("Iterating through my_tuple:")
for item in my_tuple:
    print(item)

# Tuple Usage - Function returning multiple values using a tuple
# Write a function that returns multiple values using a tuple.
# Call the function and print the returned tuple.
def get_user_info():
    name = "Alice"
    age = 30
    country = "Wonderland"
    return name, age, country  # This is a tuple being returned

user_info = get_user_info()
print("Returned Tuple from Function:", user_info)

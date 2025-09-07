A data structure is a group of data elements grouped under one name (e.g., an array of integers). The data structure gives a way of storing and organizing data in a computer so that it can be used efficiently and effectively. How different data structures can produce different approaches to a solution can be seen here: [[List solution vs. dict solution vs. generator solution]]
## Python Collections
There are four collection data types in the Python programming language:
- A list is a collection that is ordered and changeable. Allows duplicate members.
- Tuple is a collection that is ordered and unchangeable. Allows duplicate members.
- Set is a collection that is unordered and unindexed. No duplicate members.
- A dictionary is a collection that is ordered (from Python 3.7) and changeable. No duplicate members.
### List
- an ordered sequence of information, accessible by index
- a list is denoted by square brackets, []
- a list contains elements
	- usually homogeneous (i.e., all *integers*)
	- can contain mixed types (not common)

For an easy way of creating lists look at [[List comprehension]]
### Tuple
- an ordered sequence of elements, which can be of mixed element types
- a tuple is denoted by parentheses, ()
### Set
- The set is a Python implementation of the set in Mathematics. 
- A set object contains one or more items, not necessarily of the same type, which are separated by a comma and enclosed in curly brackets {} or set().
- A set does not store duplicate objects.
- Sets are unordered.
- A set itself may be modified, but the elements contained in the set must be of an immutable type.
### Dictionary
- A dictionary is like a list:
	- List: indices have to be integers
	- Dictionary: indices can be of any type
- A dictionary is defined like this, dict(). Can also be defined with curly brackets, then it is automatically evaluated if the data structure is a set or a dictionary, depending on the data inside.
- The dictionary allows mapping between a set of indices (keys) and a set of values. Each key maps to a value.
- The association of a key and a value is called a key-value pair.
### Arrays
- Arrays in Python are a compact way of collecting basic data types. All the entries in an array must be of the same data type.
- Arrays are not all that popular in Python, unlike the other programming languages such as C++ or Java.
- For Python, you need to import a module named "array".
- array(data type, value list): create an array with data type and value list specified in its arguments.

## Which Data Structure to Use in Your Program?
### Arrays Vs Lists
- Lists can hold homogeneous items, similar to arrays
- Fundamentally different in terms of the operations that can be performed on them.
	- Arrays: operations can be performed on all its items individually
	- Lists: cannot perform operations on all its items individually
- Arrays
	- Need to be declared
	- Very useful when dealing with a large collection of homogeneous data types. Arrays may be faster and uses less memory when compared to lists
	- Are great for numerical operations
- Lists:
	- Provides a large set of operations for managing the items contained in the list (inserting, searching, removing, extracting a subset of items, and sorting). The array structure only provides a limited set of operations for accessing the individual elements.
### Tuples Vs Lists
- Tuples are immutable. This might be useful in situations where we might pass the control to someone else but we do not want them to manipulate data in our collection.
### Sets Vs Lists
- Sets are a collection of distinct (unique) objects.
- These are useful to create lists that only hold unique values in the dataset.
- It is an unordered collection but a mutable one. This is very helpful when going through a huge dataset.
### Dictionary
- Dictionaries are useful when we need something similar to a telephone book.
- Dictionaries contain key-value pairs instead of just single elements.


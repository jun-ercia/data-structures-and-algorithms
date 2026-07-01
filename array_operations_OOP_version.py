# ============================================================
# Program Title : Basic Array Operations Using OOP
# Purpose       : This program demonstrates basic array operations
#                 using Object-Oriented Programming.
#                 Operations include make_null, is_empty, is_full,
#                 insert, delete, search, and traverse.
# Date Written  : July 1, 2026
# Language      : Python 3
# Written by    : Jun Ercia
# ============================================================


# ------------------------------------------------------------
# Class: ArrayOperations
# Purpose: Represents an array and performs basic array operations.
# ------------------------------------------------------------
class ArrayOperations:

    # --------------------------------------------------------
    # Constructor
    # Purpose: Initializes the array, maximum size, and current size.
    # --------------------------------------------------------
    def __init__(self, max_size):
        # Store the maximum size of the array
        self.MAX = max_size

        # Create a fixed-size array with empty values
        self.arr = [None] * self.MAX

        # Store the current number of active elements
        self.n = 0

    # --------------------------------------------------------
    # Method: make_null
    # Purpose: Clears the array by setting the number of elements to zero.
    # --------------------------------------------------------
    def make_null(self):
        # Set the number of active elements to zero
        self.n = 0

        print("Array has been cleared.")

    # --------------------------------------------------------
    # Method: is_empty
    # Purpose: Checks if the array has no active elements.
    # --------------------------------------------------------
    def is_empty(self):
        # Return True if the array has no active elements
        return self.n == 0

    # --------------------------------------------------------
    # Method: is_full
    # Purpose: Checks if the array has reached its maximum capacity.
    # --------------------------------------------------------
    def is_full(self):
        # Return True if the current size is equal to the maximum size
        return self.n == self.MAX

    # --------------------------------------------------------
    # Method: insert
    # Purpose: Inserts a value at a specific position in the array.
    # --------------------------------------------------------
    def insert(self, value, position):

        # Check if the array is already full
        if self.is_full():
            print("Array is full.")
            return

        # Check if the given position is valid
        if position < 0 or position > self.n:
            print("Invalid position.")
            return

        # Shift elements to the right to make space for the new value
        for i in range(self.n - 1, position - 1, -1):
            self.arr[i + 1] = self.arr[i]

        # Insert the new value at the given position
        self.arr[position] = value

        # Increase the number of active elements
        self.n += 1

        print(value, "inserted at position", position)

    # --------------------------------------------------------
    # Method: delete
    # Purpose: Deletes an element from a specific position in the array.
    # --------------------------------------------------------
    def delete(self, position):

        # Check if the array is empty
        if self.is_empty():
            print("Array is empty.")
            return

        # Check if the given position is valid
        if position < 0 or position >= self.n:
            print("Invalid position.")
            return

        # Store the value to be deleted
        removed_value = self.arr[position]

        # Shift elements to the left to close the gap
        for i in range(position, self.n - 1):
            self.arr[i] = self.arr[i + 1]

        # Remove the duplicate value at the last active position
        self.arr[self.n - 1] = None

        # Decrease the number of active elements
        self.n -= 1

        print(removed_value, "deleted from position", position)

    # --------------------------------------------------------
    # Method: search
    # Purpose: Searches for a value in the array using linear search.
    # --------------------------------------------------------
    def search(self, value):

        # Visit each active element in the array
        for i in range(self.n):

            # Check if the current element is equal to the search value
            if self.arr[i] == value:
                return i

        # Return -1 if the value is not found
        return -1

    # --------------------------------------------------------
    # Method: traverse
    # Purpose: Displays all active elements in the array.
    # --------------------------------------------------------
    def traverse(self):

        # Check if the array is empty
        if self.is_empty():
            print("Array is empty.")
            return

        print("Array elements:")

        # Display each active element
        for i in range(self.n):
            print(self.arr[i])


# ============================================================
# Main Program
# ============================================================

# Create an object of ArrayOperations with a maximum size of 5
my_array = ArrayOperations(5)

# Insert values into the array
my_array.insert(10, 0)
my_array.insert(20, 1)
my_array.insert(30, 2)
my_array.insert(40, 3)

print()

# Display the current array elements
my_array.traverse()

print()

# Insert 15 at position 2
my_array.insert(15, 2)

print()

# Display the array after insertion
my_array.traverse()

print()

# Delete the value at position 1
my_array.delete(1)

print()

# Display the array after deletion
my_array.traverse()

print()

# Search for a specific value
value = 30
result = my_array.search(value)

# Display the search result
if result != -1:
    print(value, "is found at index", result)
else:
    print(value, "is not found.")

print()

# Clear the array
my_array.make_null()

print()

# Display the array after make_null operation
my_array.traverse()

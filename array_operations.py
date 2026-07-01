# ============================================================
# Program Title : Basic Array Operations
# Purpose       : This program demonstrates basic array operations
#                 such as make_null, is_empty, is_full, insert,
#                 delete, search, and traverse using Python.
# Date Written  : July 1, 2026
# Language      : Python 3
# Written by    : Jun Ercia
# ============================================================

# Set the maximum size of the array
MAX = 5

# Create a fixed-size array with empty values
arr = [None] * MAX

# Store the current number of active elements in the array
n = 0


# ------------------------------------------------------------
# Function: make_null
# Purpose : Clears the array by setting the number of elements to zero.
# ------------------------------------------------------------
def make_null():
    global n

    # Set the number of active elements to zero
    n = 0

    print("Array has been cleared.")


# ------------------------------------------------------------
# Function: is_empty
# Purpose : Checks if the array has no active elements.
# ------------------------------------------------------------
def is_empty():
    # Return True if n is equal to zero
    return n == 0


# ------------------------------------------------------------
# Function: is_full
# Purpose : Checks if the array has reached its maximum capacity.
# ------------------------------------------------------------
def is_full():
    # Return True if n is equal to MAX
    return n == MAX


# ------------------------------------------------------------
# Function: insert
# Purpose : Inserts a value at a specific position in the array.
# ------------------------------------------------------------
def insert(value, position):
    global n

    # Check if the array is already full
    if is_full():
        print("Array is full.")
        return

    # Check if the given position is valid
    if position < 0 or position > n:
        print("Invalid position.")
        return

    # Shift elements to the right to make space for the new value
    for i in range(n - 1, position - 1, -1):
        arr[i + 1] = arr[i]

    # Insert the new value at the given position
    arr[position] = value

    # Increase the number of active elements
    n += 1

    print(value, "inserted at position", position)


# ------------------------------------------------------------
# Function: delete
# Purpose : Deletes an element from a specific position in the array.
# ------------------------------------------------------------
def delete(position):
    global n

    # Check if the array is empty
    if is_empty():
        print("Array is empty.")
        return

    # Check if the given position is valid
    if position < 0 or position >= n:
        print("Invalid position.")
        return

    # Store the value that will be deleted
    removed_value = arr[position]

    # Shift elements to the left to close the gap
    for i in range(position, n - 1):
        arr[i] = arr[i + 1]

    # Remove the duplicate value at the last active position
    arr[n - 1] = None

    # Decrease the number of active elements
    n -= 1

    print(removed_value, "deleted from position", position)


# ------------------------------------------------------------
# Function: search
# Purpose : Searches for a value in the array using linear search.
# ------------------------------------------------------------
def search(value):
    # Visit each active element in the array
    for i in range(n):

        # Check if the current element is equal to the search value
        if arr[i] == value:
            return i

    # Return -1 if the value is not found
    return -1


# ------------------------------------------------------------
# Function: traverse
# Purpose : Displays all active elements in the array.
# ------------------------------------------------------------
def traverse():
    # Check if the array is empty
    if is_empty():
        print("Array is empty.")
        return

    print("Array elements:")

    # Display each active element
    for i in range(n):
        print(arr[i])


# ============================================================
# Sample Program Execution
# ============================================================

# Insert values into the array
insert(10, 0)
insert(20, 1)
insert(30, 2)
insert(40, 3)

# Display the current array elements
traverse()

# Insert 15 at position 2
insert(15, 2)

print()

# Display the array after insertion
traverse()

# Delete the value at position 1
delete(1)

print()

# Display the array after deletion
traverse()

# Search for a specific value
value = 30
result = search(value)

print()

# Display the search result
if result != -1:
    print(value, "is found at index", result)
else:
    print(value, "is not found.")

# Clear the array
make_null()

print()

# Display the array after make_null operation
traverse()


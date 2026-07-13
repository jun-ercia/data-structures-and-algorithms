# ============================================================
# Program Title : Stack ADT Using Array
# Purpose       : This program demonstrates basic stack
#                 operations such as push, pop, peek,
#                 is_empty, and size using an array.
# Date Written  : July 2026
# Language      : Python 3
# Written by    : Jun Ercia
# ============================================================


# ------------------------------------------------------------
# Class: ArrayStack
# Purpose: Represents a stack using an array/list.
# ------------------------------------------------------------
class ArrayStack:

    def __init__(self, max_size):
        # Maximum number of elements allowed in the stack
        self.MAX = max_size

        # Create an empty array with fixed size
        self.stack = [None] * self.MAX

        # TOP is -1 when the stack is empty
        self.TOP = -1

    # --------------------------------------------------------
    # Method: is_empty
    # Purpose: Checks if the stack has no elements.
    # --------------------------------------------------------
    def is_empty(self):
        return self.TOP == -1

    # --------------------------------------------------------
    # Method: is_full
    # Purpose: Checks if the stack is already full.
    # --------------------------------------------------------
    def is_full(self):
        return self.TOP == self.MAX - 1

    # --------------------------------------------------------
    # Method: push
    # Purpose: Adds a new item to the top of the stack.
    # --------------------------------------------------------
    def push(self, value):

        # Check for stack overflow
        if self.is_full():
            print("Stack Overflow. Cannot push", value)
            return

        # Move TOP upward
        self.TOP += 1

        # Store the value at the top position
        self.stack[self.TOP] = value

        print(value, "pushed into the stack.")

    # --------------------------------------------------------
    # Method: pop
    # Purpose: Removes and returns the top item of the stack.
    # --------------------------------------------------------
    def pop(self):

        # Check for stack underflow
        if self.is_empty():
            print("Stack Underflow. Cannot pop from an empty stack.")
            return None

        # Get the top item
        item = self.stack[self.TOP]

        # Optional: clear the removed position
        self.stack[self.TOP] = None

        # Move TOP downward
        self.TOP -= 1

        print(item, "popped from the stack.")
        return item

    # --------------------------------------------------------
    # Method: peek
    # Purpose: Displays the top item without removing it.
    # --------------------------------------------------------
    def peek(self):

        if self.is_empty():
            print("Stack is empty.")
            return None

        return self.stack[self.TOP]

    # --------------------------------------------------------
    # Method: size
    # Purpose: Returns the number of elements in the stack.
    # --------------------------------------------------------
    def size(self):
        return self.TOP + 1

    # --------------------------------------------------------
    # Method: display
    # Purpose: Displays the stack from top to bottom.
    # --------------------------------------------------------
    def display(self):

        if self.is_empty():
            print("Stack is empty.")
            return

        print("Stack elements from TOP to BOTTOM:")

        for i in range(self.TOP, -1, -1):
            print(self.stack[i])


# ------------------------------------------------------------
# Main Program for Array-Based Stack
# ------------------------------------------------------------
stack = ArrayStack(5)

while True:
    print("\n========================================")
    print("ARRAY-BASED STACK MENU")
    print("========================================")
    print("[1] Push")
    print("[2] Pop")
    print("[3] Peek")
    print("[4] Check if Empty")
    print("[5] Check Size")
    print("[6] Display Stack")
    print("[7] Exit")
    print("========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        value = input("Enter value to push: ")
        stack.push(value)

    elif choice == "2":
        stack.pop()

    elif choice == "3":
        top_value = stack.peek()

        if top_value is not None:
            print("Top element is:", top_value)

    elif choice == "4":
        if stack.is_empty():
            print("Stack is empty.")
        else:
            print("Stack is not empty.")

    elif choice == "5":
        print("Stack size:", stack.size())

    elif choice == "6":
        stack.display()

    elif choice == "7":
        print("Program ended. Thank you!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 7.")

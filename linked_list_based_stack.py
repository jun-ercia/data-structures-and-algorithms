# ============================================================
# Program Title : Stack ADT Using Linked List
# Purpose       : This program demonstrates basic stack
#                 operations such as push, pop, peek,
#                 is_empty, and size using a linked list.
# Date Written  : July 2026
# Language      : Python 3
# Written by    : Jun Ercia
# ============================================================


# ------------------------------------------------------------
# Class: Node
# Purpose: Represents one node in the linked list stack.
# ------------------------------------------------------------
class Node:

    def __init__(self, data):
        # Store the value of the node
        self.data = data

        # Store the address of the next node
        self.next = None


# ------------------------------------------------------------
# Class: LinkedListStack
# Purpose: Represents a stack using a linked list.
# ------------------------------------------------------------
class LinkedListStack:

    def __init__(self):
        # TOP points to the first node of the stack
        self.TOP = None

    # --------------------------------------------------------
    # Method: is_empty
    # Purpose: Checks if the stack has no nodes.
    # --------------------------------------------------------
    def is_empty(self):
        return self.TOP is None

    # --------------------------------------------------------
    # Method: push
    # Purpose: Adds a new item to the top of the stack.
    # --------------------------------------------------------
    def push(self, value):

        # Create a new node
        new_node = Node(value)

        # The new node points to the current TOP
        new_node.next = self.TOP

        # TOP is updated to the new node
        self.TOP = new_node

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

        # Store the top value
        item = self.TOP.data

        # Move TOP to the next node
        self.TOP = self.TOP.next

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

        return self.TOP.data

    # --------------------------------------------------------
    # Method: size
    # Purpose: Counts the number of nodes in the stack.
    # --------------------------------------------------------
    def size(self):

        count = 0
        temp = self.TOP

        while temp is not None:
            count += 1
            temp = temp.next

        return count

    # --------------------------------------------------------
    # Method: display
    # Purpose: Displays the stack from top to bottom.
    # --------------------------------------------------------
    def display(self):

        if self.is_empty():
            print("Stack is empty.")
            return

        temp = self.TOP

        print("Stack elements from TOP to BOTTOM:")

        while temp is not None:
            print(temp.data)
            temp = temp.next


# ------------------------------------------------------------
# Main Program for Linked List-Based Stack
# ------------------------------------------------------------
stack = LinkedListStack()

while True:
    print("\n========================================")
    print("LINKED LIST-BASED STACK MENU")
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

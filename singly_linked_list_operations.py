# ============================================================
# Program Title : Basic Operations in Singly Linked List
# Purpose       : This program demonstrates basic operations
#                 in a singly linked list such as make_null,
#                 is_empty, insert_at_end, delete_by_value,
#                 search, and traverse.
# Date Written  : July 1, 2026
# Language      : Python 3
# Written by    : Jun Ercia
# ============================================================


# ------------------------------------------------------------
# Class: Node
# Purpose: Represents one node in the linked list.
# Each node contains data and a pointer to the next node.
# ------------------------------------------------------------
class Node:

    def __init__(self, data):
        # Store the value of the node
        self.data = data

        # Store the address of the next node
        self.next = None


# ------------------------------------------------------------
# Class: SinglyLinkedList
# Purpose: Represents the linked list and its operations.
# ------------------------------------------------------------
class SinglyLinkedList:

    def __init__(self):
        # The head points to the first node of the linked list
        self.head = None

    # --------------------------------------------------------
    # Method: make_null
    # Purpose: Clears the linked list by setting head to None.
    # --------------------------------------------------------
    def make_null(self):
        self.head = None
        print("Linked list has been cleared.")

    # --------------------------------------------------------
    # Method: is_empty
    # Purpose: Checks if the linked list has no nodes.
    # --------------------------------------------------------
    def is_empty(self):
        return self.head is None

    # --------------------------------------------------------
    # Method: insert_at_end
    # Purpose: Inserts a new node at the end of the linked list.
    # --------------------------------------------------------
    def insert_at_end(self, value):

        # Create a new node
        new_node = Node(value)

        # If the list is empty, the new node becomes the head
        if self.head is None:
            self.head = new_node
            print(value, "inserted as the first node.")
            return

        # Start from the head node
        temp = self.head

        # Move until the last node is reached
        while temp.next is not None:
            temp = temp.next

        # Connect the last node to the new node
        temp.next = new_node

        print(value, "inserted at the end.")

    # --------------------------------------------------------
    # Method: delete_by_value
    # Purpose: Deletes the first node that contains the given value.
    # --------------------------------------------------------
    def delete_by_value(self, value):

        # Check if the list is empty
        if self.head is None:
            print("List is empty.")
            return

        # Check if the value is found at the head node
        if self.head.data == value:
            self.head = self.head.next
            print(value, "deleted from the list.")
            return

        # Use two pointers: prev and curr
        prev = self.head
        curr = self.head.next

        # Search for the value in the list
        while curr is not None and curr.data != value:
            prev = curr
            curr = curr.next

        # If curr becomes None, the value was not found
        if curr is None:
            print("Value not found.")
        else:
            # Skip the current node to delete it
            prev.next = curr.next
            print(value, "deleted from the list.")

    # --------------------------------------------------------
    # Method: search
    # Purpose: Searches for a value and returns its index.
    # --------------------------------------------------------
    def search(self, value):

        # Start at index 0
        index = 0

        # Start from the head node
        temp = self.head

        # Traverse the linked list
        while temp is not None:

            # Check if the current node contains the value
            if temp.data == value:
                return index

            # Move to the next node
            temp = temp.next

            # Increase the index
            index += 1

        # Return -1 if the value is not found
        return -1

    # --------------------------------------------------------
    # Method: traverse
    # Purpose: Displays all values in the linked list.
    # --------------------------------------------------------
    def traverse(self):

        # Check if the list is empty
        if self.head is None:
            print("List is empty.")
            return

        # Start from the head node
        temp = self.head

        print("Linked list elements:")

        # Visit each node until the end of the list
        while temp is not None:
            print(temp.data)
            temp = temp.next


# ============================================================
# Main Program
# ============================================================

# Create a linked list object
linked_list = SinglyLinkedList()

# Insert values at the end of the linked list
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)

print()

# Display all values
linked_list.traverse()

print()

# Search for a value
value = 20
result = linked_list.search(value)

if result != -1:
    print(value, "is found at index", result)
else:
    print(value, "is not found.")

print()

# Delete a value from the linked list
linked_list.delete_by_value(20)

print()

# Display the linked list after deletion
linked_list.traverse()

print()

# Clear the linked list
linked_list.make_null()

print()

# Display the linked list after make_null
linked_list.traverse()

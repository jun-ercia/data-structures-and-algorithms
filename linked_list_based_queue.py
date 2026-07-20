# ============================================================
# Program Title : Linked List-Based Queue Implementation
# Purpose       : Demonstrates Queue ADT operations using
#                 a singly linked list.
# Language      : Python 3
# ============================================================


# ------------------------------------------------------------
# Class: Node
# Purpose: Represents one element in the linked list queue.
# ------------------------------------------------------------
class Node:

    def __init__(self, data):
        # Store the value of the node
        self.data = data

        # Reference to the next node
        self.next = None


# ------------------------------------------------------------
# Class: LinkedQueue
# Purpose: Implements Queue ADT using a linked list.
# ------------------------------------------------------------
class LinkedQueue:

    def __init__(self):
        # FRONT points to the first node
        self.FRONT = None

        # REAR points to the last node
        self.REAR = None

    # --------------------------------------------------------
    # Method: is_empty
    # Purpose: Checks whether the queue has no nodes.
    # --------------------------------------------------------
    def is_empty(self):
        return self.FRONT is None

    # --------------------------------------------------------
    # Method: enqueue
    # Purpose: Adds a new node at the rear of the queue.
    # --------------------------------------------------------
    def enqueue(self, value):

        # Create a new node containing the value
        new_node = Node(value)

        # If the queue is empty, both FRONT and REAR
        # point to the new node
        if self.is_empty():
            self.FRONT = new_node
            self.REAR = new_node

        else:
            # Connect the current rear node to the new node
            self.REAR.next = new_node

            # Move REAR to the new node
            self.REAR = new_node

        print(value, "enqueued successfully.")

    # --------------------------------------------------------
    # Method: dequeue
    # Purpose: Removes and returns the front element.
    # --------------------------------------------------------
    def dequeue(self):

        # Check for queue underflow
        if self.is_empty():
            print("Queue Underflow. Cannot dequeue from an empty queue.")
            return None

        # Save the front node temporarily
        temp = self.FRONT

        # Get the value stored in the front node
        item = temp.data

        # Move FRONT to the next node
        self.FRONT = self.FRONT.next

        # If the queue becomes empty, reset REAR
        if self.FRONT is None:
            self.REAR = None

        # Disconnect the removed node
        temp.next = None

        print(item, "dequeued successfully.")
        return item

    # --------------------------------------------------------
    # Method: peek
    # Purpose: Returns the front element without removing it.
    # --------------------------------------------------------
    def peek(self):

        if self.is_empty():
            print("Queue is empty.")
            return None

        return self.FRONT.data

    # --------------------------------------------------------
    # Method: size
    # Purpose: Counts and returns the number of nodes.
    # --------------------------------------------------------
    def size(self):

        count = 0
        current = self.FRONT

        # Traverse the linked list
        while current is not None:
            count += 1
            current = current.next

        return count

    # --------------------------------------------------------
    # Method: display
    # Purpose: Displays elements from FRONT to REAR.
    # --------------------------------------------------------
    def display(self):

        if self.is_empty():
            print("Queue is empty.")
            return

        print("Queue elements from FRONT to REAR:")

        current = self.FRONT

        while current is not None:
            print(current.data, end=" ")

            if current.next is not None:
                print("->", end=" ")

            current = current.next

        print()

    # --------------------------------------------------------
    # Method: display_structure
    # Purpose: Displays the linked-list queue structure.
    # --------------------------------------------------------
    def display_structure(self):

        if self.is_empty():
            print("FRONT = None")
            print("REAR  = None")
            print("Queue is empty.")
            return

        print("\nLinked List Queue Structure:")
        print("FRONT")

        current = self.FRONT

        while current is not None:
            print("  ↓")
            print("[", current.data, "| NEXT ]", sep="")

            if current.next is not None:
                print("  ↓")

            current = current.next

        print("  ↓")
        print("NULL")
        print("REAR points to:", self.REAR.data)

    # --------------------------------------------------------
    # Method: clear
    # Purpose: Removes all nodes from the queue.
    # --------------------------------------------------------
    def clear(self):

        current = self.FRONT

        # Disconnect every node
        while current is not None:
            next_node = current.next
            current.next = None
            current = next_node

        self.FRONT = None
        self.REAR = None

        print("Queue has been cleared.")


# ------------------------------------------------------------
# Function: display_menu
# Purpose: Displays the available Queue ADT operations.
# ------------------------------------------------------------
def display_menu():

    print("\n========================================")
    print("LINKED LIST-BASED QUEUE IMPLEMENTATION")
    print("========================================")
    print("[1] Enqueue")
    print("[2] Dequeue")
    print("[3] Peek")
    print("[4] Display Queue")
    print("[5] Check if Queue is Empty")
    print("[6] Display Queue Size")
    print("[7] Display Linked List Structure")
    print("[8] Clear Queue")
    print("[9] Exit")
    print("========================================")


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------
def main():

    queue = LinkedQueue()

    while True:

        try:
            display_menu()

            choice = int(input("Enter your choice: "))

            # ------------------------------------------------
            # Option 1: Enqueue
            # ------------------------------------------------
            if choice == 1:

                value = input("Enter value to enqueue: ").strip()

                if value == "":
                    print("Value cannot be blank.")
                else:
                    queue.enqueue(value)

            # ------------------------------------------------
            # Option 2: Dequeue
            # ------------------------------------------------
            elif choice == 2:
                queue.dequeue()

            # ------------------------------------------------
            # Option 3: Peek
            # ------------------------------------------------
            elif choice == 3:

                front_item = queue.peek()

                if front_item is not None:
                    print("Front element:", front_item)

            # ------------------------------------------------
            # Option 4: Display Queue
            # ------------------------------------------------
            elif choice == 4:
                queue.display()

            # ------------------------------------------------
            # Option 5: Check if Queue Is Empty
            # ------------------------------------------------
            elif choice == 5:

                if queue.is_empty():
                    print("The queue is empty.")
                else:
                    print("The queue is not empty.")

            # ------------------------------------------------
            # Option 6: Display Queue Size
            # ------------------------------------------------
            elif choice == 6:
                print("Queue size:", queue.size())

            # ------------------------------------------------
            # Option 7: Display Linked List Structure
            # ------------------------------------------------
            elif choice == 7:
                queue.display_structure()

            # ------------------------------------------------
            # Option 8: Clear Queue
            # ------------------------------------------------
            elif choice == 8:
                queue.clear()

            # ------------------------------------------------
            # Option 9: Exit Program
            # ------------------------------------------------
            elif choice == 9:
                print("Program ended. Thank you!")
                break

            # ------------------------------------------------
            # Invalid menu number
            # ------------------------------------------------
            else:
                print(
                    "Invalid menu choice. "
                    "Please enter a number from 1 to 9."
                )

        # Handles letters, symbols, decimal values, and blanks
        except ValueError:
            print(
                "Invalid input. Please enter a whole number "
                "from 1 to 9."
            )

        # Handles Ctrl+C
        except KeyboardInterrupt:
            print("\nProgram interrupted by the user.")
            print("Program ended. Thank you!")
            break

        # Handles an unexpected end of input
        except EOFError:
            print("\nNo more input was received.")
            print("Program ended. Thank you!")
            break

        # Handles other unexpected errors
        except Exception as error:
            print("An unexpected error occurred:", error)


# Run the main program
if __name__ == "__main__":
    main()


# ============================================================
# Program Title : Array-Based Queue Implementation
# Purpose       : Demonstrates Queue ADT operations using a
#                 fixed-size array.
# Language      : Python 3
# ============================================================


class ArrayQueue:

    def __init__(self, max_size):
        """Creates an empty queue with a fixed maximum size."""

        if not isinstance(max_size, int):
            raise TypeError("Maximum size must be an integer.")

        if max_size <= 0:
            raise ValueError("Maximum size must be greater than zero.")

        # Maximum number of elements allowed in the queue
        self.MAX = max_size

        # Fixed-size array used to store queue elements
        self.Q = [None] * self.MAX

        # FRONT and REAR are -1 when the queue is empty
        self.FRONT = -1
        self.REAR = -1

    # --------------------------------------------------------
    # Method: is_empty
    # Purpose: Checks whether the queue has no elements.
    # --------------------------------------------------------
    def is_empty(self):
        return self.FRONT == -1 or self.FRONT > self.REAR

    # --------------------------------------------------------
    # Method: is_full
    # Purpose: Checks whether REAR reached the final index.
    # --------------------------------------------------------
    def is_full(self):
        return self.REAR == self.MAX - 1

    # --------------------------------------------------------
    # Method: enqueue
    # Purpose: Adds a new element at the rear of the queue.
    # --------------------------------------------------------
    def enqueue(self, value):

        # Check for queue overflow
        if self.is_full():
            print("Queue Overflow. Cannot enqueue", value)
            return False

        # Set FRONT to the first index when inserting the
        # first element
        if self.FRONT == -1:
            self.FRONT = 0

        # Move REAR forward
        self.REAR += 1

        # Store the new value at REAR
        self.Q[self.REAR] = value

        print(value, "enqueued successfully.")
        return True

    # --------------------------------------------------------
    # Method: dequeue
    # Purpose: Removes and returns the front element.
    # --------------------------------------------------------
    def dequeue(self):

        # Check for queue underflow
        if self.is_empty():
            print("Queue Underflow. Cannot dequeue from an empty queue.")
            return None

        # Get the element at FRONT
        item = self.Q[self.FRONT]

        # Clear the removed position
        self.Q[self.FRONT] = None

        # Move FRONT forward
        self.FRONT += 1

        # Reset the queue when the last element is removed
        if self.FRONT > self.REAR:
            self.FRONT = -1
            self.REAR = -1

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

        return self.Q[self.FRONT]

    # --------------------------------------------------------
    # Method: size
    # Purpose: Returns the number of elements in the queue.
    # --------------------------------------------------------
    def size(self):

        if self.is_empty():
            return 0

        return self.REAR - self.FRONT + 1

    # --------------------------------------------------------
    # Method: display
    # Purpose: Displays queue elements from FRONT to REAR.
    # --------------------------------------------------------
    def display(self):

        if self.is_empty():
            print("Queue is empty.")
            return

        print("\nQueue elements from FRONT to REAR:")

        for index in range(self.FRONT, self.REAR + 1):
            print(self.Q[index], end=" ")

        print()
        print("FRONT =", self.FRONT)
        print("REAR  =", self.REAR)

    # --------------------------------------------------------
    # Method: display_array
    # Purpose: Displays all positions in the fixed-size array.
    # --------------------------------------------------------
    def display_array(self):
        print("Queue Array:", self.Q)
        print("FRONT =", self.FRONT)
        print("REAR  =", self.REAR)

    # --------------------------------------------------------
    # Method: clear
    # Purpose: Removes all elements from the queue.
    # --------------------------------------------------------
    def clear(self):

        for index in range(self.MAX):
            self.Q[index] = None

        self.FRONT = -1
        self.REAR = -1

        print("Queue has been cleared.")


# ============================================================
# Main Program
# ============================================================

try:
    queue = ArrayQueue(5)

    while True:
        print("\n========================================")
        print("ARRAY-BASED QUEUE IMPLEMENTATION")
        print("========================================")
        print("[1] Enqueue")
        print("[2] Dequeue")
        print("[3] Peek")
        print("[4] Display Queue")
        print("[5] Check if Queue is Empty")
        print("[6] Check if Queue is Full")
        print("[7] Display Queue Size")
        print("[8] Display Complete Array")
        print("[9] Clear Queue")
        print("[10] Exit")
        print("========================================")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                value = input("Enter value to enqueue: ").strip()

                if value == "":
                    print("Value cannot be blank.")
                else:
                    queue.enqueue(value)

            elif choice == 2:
                queue.dequeue()

            elif choice == 3:
                front_item = queue.peek()

                if front_item is not None:
                    print("Front element:", front_item)

            elif choice == 4:
                queue.display()

            elif choice == 5:
                if queue.is_empty():
                    print("The queue is empty.")
                else:
                    print("The queue is not empty.")

            elif choice == 6:
                if queue.is_full():
                    print("The queue is full.")
                else:
                    print("The queue is not full.")

            elif choice == 7:
                print("Queue size:", queue.size())

            elif choice == 8:
                queue.display_array()

            elif choice == 9:
                queue.clear()

            elif choice == 10:
                print("Program ended. Thank you!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 10.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

        except KeyboardInterrupt:
            print("\nProgram interrupted by the user.")
            break

        except EOFError:
            print("\nNo more input was received.")
            break

except (TypeError, ValueError) as error:
    print("Queue creation error:", error)

except Exception as error:
    print("An unexpected error occurred:", error)

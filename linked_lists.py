# A Node class represents an individual element in the linked list.
# It contains two parts: the data, and the reference (pointer) to the next node.
class Node:
    def __init__(self, data):
        self.data = data    # Stores the actual data
        self.next = None    # Points to the next node (initially None)

# LinkedList class handles the operations on the list such as insertion, deletion, and search.
class LinkedList:
    def __init__(self):
        self.head = None  # The head node marks the start of the list

    # Insert a node at the beginning of the list
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)     # Create a new node with the given data
        new_node.next = self.head     # Point the new node to the current head
        self.head = new_node          # Update the head to be the new node

    # Insert a node at the end of the list
    def insertAtTheEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node      # If list is empty, new node becomes the head
            return
        last = self.head
        while last.next:              # Traverse to the last node
            last = last.next
        last.next = new_node          # Make the last node point to the new node

    # Delete a node from the beginning of the list
    def deleteFromBeginning(self):
        if self.head is None:
            return "List is empty"    # Nothing to delete
        self.head = self.head.next    # Move head to the next node

    # Delete a node from the end of the list
    def deleteFromEnd(self):
        if self.head is None:
            return "List is empty"
        if self.head.next is None:
            self.head = None          # If only one node, just remove it
            return
        temp = self.head
        while temp.next.next:         # Traverse to the second last node
            temp = temp.next
        temp.next = None              # Remove last node by pointing to None

    # Search the list for a specific value
    def search(self, value):
        current = self.head           # Start from the head
        position = 0                  # Track position of nodes
        while current:
            if current.data == value:
                return f"Value {value} found at position {position}"
            current = current.next
            position += 1
        return f"Value {value} not found in the list"

    # Print all the elements of the linked list
    def printlist(self):
        temp = self.head
        while temp:
            print(f"{temp.data} -> ", end='')  # Print node followed by arrow
            temp = temp.next
        print("None")  # End of list

# Test the LinkedList functionality
if __name__ == '__main__':
    llist = LinkedList()  # Create a new LinkedList instance

    # Insert words at the beginning
    llist.insertAtBeginning("fox")
    llist.insertAtBeginning("brown")
    llist.insertAtBeginning("quick")
    llist.insertAtBeginning("the")  # Head now becomes "the"

    llist.printlist()  # Expected: the -> quick -> brown -> fox -> None

    llist.insertAtTheEnd("jumps")  # Insert "jumps" at the end
    llist.printlist()              # Expected: the -> quick -> brown -> fox -> jumps -> None

    llist.deleteFromBeginning()    # Delete the first node ("the")
    print("List after deletion:")
    llist.printlist()              # Expected: quick -> brown -> fox -> jumps -> None

    llist.deleteFromEnd()  # Delete the first node ("the")
    print("List after deletion:")
    llist.printlist()  # Expected: quick -> brown -> fox -> jumps -> None
    # Search for a value that exists and one that doesn't
    print(llist.search("quick"))   # Should find it
    print(llist.search("lazy"))    # Should not find it





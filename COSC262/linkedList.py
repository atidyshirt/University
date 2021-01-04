
# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
                          # next as null

# Linked List class
class LinkedList:

    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None

'''
------------ Linked Lists ----------------

linked list is a series of linked nodes
to access a node, you must start at the
head, and link untill reach desired node

append to the end is inefficent O(n),
however deleting and inserting at front
of list is extremely quick O(1)

Doubly linked list:
  -> each element links to both next and
     previous elements (not just the next
     node).

------------ Linked Lists ----------------
'''

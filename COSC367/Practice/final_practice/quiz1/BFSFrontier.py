from search import *

# write a class to hold a node for a linked list node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# write a class to hold a linked list queue

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self.size += 1

    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            self.size -= 1
            return temp.data

    def isEmpty(self):
        return self.size == 0


class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = Queue()

    def add(self, path):
        """Adds a new path to the frontier."""
        self.container.enqueue(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if not self.container.isEmpty():
            return self.container.dequeue()
        else:
            raise StopIteration   # don't change this one

class FunkyNumericGraph(Graph):
    """A graph where nodes are numbers. A number n leads to n-1 and
    n+2. Nodes that are divisible by 10 are goal nodes."""

    def __init__(self, starting_number):
        self.starting_number = starting_number

    def outgoing_arcs(self, tail_node):
        """Takes a node (which is an integer in this problem) and returns
        outgoing arcs (always two arcs in this problem)"""
        return [
            Arc(tail_node, tail_node - 1, action="1down", cost=1),
            Arc(tail_node, tail_node + 2, action="2up", cost=1)
        ]

    def starting_nodes(self):
        """Returns a sequence (list) of starting nodes. In this problem
        the seqence always has one element."""
        return [self.starting_number]

    def is_goal(self, node):
        """Determine whether a given node (integer) is a goal."""
        return node % 10 == 0

graph = FunkyNumericGraph(3)
solutions = generic_search(graph, BFSFrontier())
print_actions(next(solutions))
print()
print_actions(next(solutions))

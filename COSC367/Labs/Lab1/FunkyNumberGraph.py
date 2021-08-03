from modules.search import *

class FunkyNumericGraph(Graph):
    """A graph where nodes are numbers. A number n leads to n-1 and
    n+2. Nodes that are divisible by 10 are goal nodes."""

    def __init__(self, starting_number):
        self.starting_number = starting_number

    def outgoing_arcs(self, tail_node):
        """Takes a node (which is an integer in this problem) and returns
        outgoing arcs (always two arcs in this problem)"""
        return [Arc(tail_node, tail_node-1, action="1down", cost=1),
                Arc(tail_node, tail_node+2, action="2up", cost=1)]

    def starting_nodes(self):
        """Returns a sequence (list) of starting nodes. In this problem
        the seqence always has one element."""
        return [self.starting_number]

    def is_goal(self, node):
        """Determine whether a given node (integer) is a goal."""
        return node % 10 == 0


class Node:
    """ A generic node to be used within datastructure object's

    These classes were just datastructures I had built and stored locally """
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class Queue:
    """ Class to create Queue

    These classes were just datastructures I had built and stored locally """
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.size

    def enqueue(self, data):
        """ Adds new node to tail of the queue """
        item = Node(data)
        if self.size == 0:
            self.head = item
            self.tail = item
        self.tail.next = item
        self.tail = self.tail.next
        self.size += 1

    def dequeue(self) -> Node or None:
        """ Removes and returns current head from the queue """
        if self.size == 0:
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty queue."""
        self.container = Queue()

    def add(self, path):
        self.container.enqueue(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            return self.container.dequeue()
        else:
            raise StopIteration

def main():
    graph = FunkyNumericGraph(4)
    for node in graph.starting_nodes():
        print(node)
    graph = FunkyNumericGraph(3)
    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))
    print()
    print_actions(next(solutions))

if __name__ == "__main__":
    main()


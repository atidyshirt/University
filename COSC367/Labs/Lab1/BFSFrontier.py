from modules.search import *

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
    # Example 1
    graph = ExplicitGraph(nodes=set('SAG'),
                          edge_list = [('S','A'), ('S', 'G'), ('A', 'G')],
                          starting_nodes = ['S'],
                          goal_nodes = {'G'})

    solutions = generic_search(graph, BFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)
    # Example 2
    flights = ExplicitGraph(
        nodes=[
            'Christchurch',
            'Auckland',
            'Wellington',
            'Gold Coast'
        ],
        edge_list = [
            ('Christchurch', 'Gold Coast'),
            ('Christchurch','Auckland'),
            ('Christchurch','Wellington'),
            ('Wellington', 'Gold Coast'),
            ('Wellington', 'Auckland'),
            ('Auckland', 'Gold Coast')
        ],
        starting_nodes = ['Christchurch'],
        goal_nodes = {'Gold Coast'})

    my_itinerary = next(generic_search(flights, BFSFrontier()), None)
    print_actions(my_itinerary)

if __name__ == "__main__":
    main()

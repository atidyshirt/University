from modules.search import Graph, Frontier, Arc, generic_search, print_actions
import copy

BLANK = ' '

class SlidingPuzzleGraph(Graph):
    """Objects of this type represent (n squared minus one)-puzzles.
    """
    def __init__(self, starting_state):
        self.starting_state = starting_state

    def outgoing_arcs(self, state):
        """Given a puzzle state (node) returns a list of arcs. Each arc
        represents a possible action (move) and the resulting state."""
        n = len(state) # the size of the puzzle
        i, j = next((i, j) for i in range(n) for j in range(n) if state[i][j] == BLANK) # find the blank tile
        arcs = []
        if i > 0:
            action = "Move {} down".format(state[i-1][j]) # or blank goes up
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i-1][j] = new_state[i-1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if i < n - 1:
            action = "Move {} up".format(state[i+1][j]) # or blank goes down
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i+1][j] = new_state[i+1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j > 0:
            action = "Move {} right".format(state[i][j-1]) # or blank goes left
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i][j-1] = new_state[i][j-1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j < n - 1:
            action = "Move {} left".format(state[i][j+1]) # or blank goes left
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i][j+1] = new_state[i][j+1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        return arcs

    def starting_nodes(self):
        return [self.starting_state]

    def is_goal(self, state):
        """Returns true if the given state is the goal state, False
        otherwise. There is only one goal state in this problem."""
        n = len(state)
        current = 0
        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0:
                    if state[i][j] != BLANK: # checks if the first tile is not blank
                        return False
                else:
                    if state[i][j] <= current: # checks if the tiles are in order
                        return False
                    else:
                        current = state[i][j]
        return True

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
    graph = SlidingPuzzleGraph([[1, 2, 5],
                                [3, 4, 8],
                                [6, 7, ' ']])
    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))

if __name__ == "__main__":
    main()


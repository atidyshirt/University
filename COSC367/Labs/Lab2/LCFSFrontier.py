import heapq
from search import *


class LocationGraph(ExplicitGraph):
    def __init__(self, nodes, locations, edges, starting_nodes, goal_nodes, estimates=None):
        """Initialises an location graph."""
        # Checks
        assert all(tail in nodes and head in nodes for tail, head, *_ in edges)\
           , "An edge must link two existing nodes!"
        assert all(node in nodes for node in starting_nodes),\
            "The starting_states must be in nodes."
        assert all(node in nodes for node in goal_nodes),\
            "The goal states must be in nodes."
        self.nodes = nodes
        self.locations = locations
        self.edges = edges
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes
        self.estimates = estimates

    def outgoing_arcs(self, node):
        """Returns a sequence of Arc objects that go out from the given
        node. The action string is automatically generated.
        """
        arcs = []
        for edge in self.edges:
            if len(edge) == 2:
                tail, head = edge
                cost = ((self.locations[edge[1]][0] - self.locations[edge[0]][0])**2 + (self.locations[edge[1]][1] - self.locations[edge[0]][1])**2)**(1/2)
            else:
                tail, head, cost = edge
            if head == node and Arc(head, tail, str(head) + '->' + str(tail), cost) not in arcs:
                arcs.append(Arc(head, tail, str(head) + '->' + str(tail), cost))
            if tail == node and Arc(tail, head, str(tail) + '->' + str(head), cost) not in arcs:
                arcs.append(Arc(tail, head, str(tail) + '->' + str(head), cost))
        return sorted(arcs, key=lambda arc: (arc.tail, arc.head))


class LCFSFrontier(Frontier):
    """Implements an LCFS frontier container"""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.heap = []

    def add(self, path):
        heapq.heappush(self.heap, path)

    def __next__(self):
        if len(self.heap) > 0:
            return heapq.heappop(self.heap)
        else:
            raise StopIteration


if __name__ == '__main__':
    print("")
    print("---------------------------------")
    print("")

    graph = LocationGraph(nodes=set('ABC'),
                          locations={'A': (0, 0),
                                     'B': (3, 0),
                                     'C': (3, 4)},
                          edges={('A', 'B'), ('B','C'),
                                 ('B', 'A'), ('C', 'A')},
                          starting_nodes=['A'],
                          goal_nodes={'C'})

    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)

    print("")
    print("---------------------------------")
    print("")

    graph = LocationGraph(nodes=set('ABC'),
                          locations={'A': (0, 0),
                                     'B': (3, 0),
                                     'C': (3, 4)},
                          edges={('A', 'B'), ('B','C'),
                                 ('B', 'A')},
                          starting_nodes=['A'],
                          goal_nodes={'C'})

    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)

    print("")
    print("---------------------------------")
    print("")

    pythagorean_graph = LocationGraph(
        nodes=set("abc"),
        locations={'a': (5, 6),
                   'b': (10,6),
                   'c': (10,18)},
        edges={tuple(s) for s in {'ab', 'ac', 'bc'}},
        starting_nodes=['a'],
        goal_nodes={'c'})

    solution = next(generic_search(pythagorean_graph, LCFSFrontier()))
    print_actions(solution)

    print("")
    print("---------------------------------")
    print("")

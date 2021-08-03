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

if __name__ == '__main__':
    graph = LocationGraph(nodes=set('ABC'),
                          locations={'A': (0, 0),
                                     'B': (3, 0),
                                     'C': (3, 4)},
                          edges={('A', 'B'), ('B','C'),
                                 ('C', 'A')},
                          starting_nodes=['A'],
                          goal_nodes={'C'})

    for arc in graph.outgoing_arcs('A'):
        print(arc)
    for arc in graph.outgoing_arcs('B'):
        print(arc)
    for arc in graph.outgoing_arcs('C'):
        print(arc)

from search import *
import heapq


class LCFSFrontier(Frontier):
    """Implements a frontier appropriate for lowest-cost-first."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []
        heapq.heapify(self.container)


    def add(self, path):
        """Add a new path to the frontier."""
        total_cost = 0
        for node in path:
            total_cost += node.cost
        heapq.heappush(self.container, (total_cost, path))


    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            return heapq.heappop(self.container)[-1]
        else:
            raise StopIteration   # don't change this one


graph = ExplicitGraph(
    nodes = {'S', 'A', 'B', 'G'},
    edge_list=[('S','A',3), ('S','B',1), ('B','A',1), ('A','B',1), ('A','G',5)],
    starting_nodes = ['S'],
    goal_nodes = {'G'})

solution = next(generic_search(graph, LCFSFrontier()))
print_actions(solution)

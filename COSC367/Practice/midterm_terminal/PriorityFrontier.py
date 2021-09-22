from resources.search import *


class PriorityFrontier(Frontier):
    def __init__(self):
        self.container = []
        self.visited = set()


    def add(self, path):
        raise NotImplementedError # FIX THIS: Replace it with proper code

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional information for iteration."""
        return self

    def __next__(self):
        # Complete
        raise StopIteration   # raise this when the container is exhuasted


graph = ExplicitGraph(
    nodes = {'S', 'A', 'B', 'G'},
    edge_list=[('S','A',3), ('S','B',1), ('B','A',1), ('A','B',1), ('A','G',5)],
    starting_nodes = ['S'],
    goal_nodes = {'G'})

solution = next(generic_search(graph, PriorityFrontier()))
print_actions(solution)

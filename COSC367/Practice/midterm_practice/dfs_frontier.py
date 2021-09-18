from resources.search import *


class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            return self.container.pop()
        else:
            raise StopIteration   # don't change this one

available_flights = ExplicitGraph(
    nodes=['Christchurch', 'Auckland',
           'Wellington', 'Gold Coast'],
    edge_list=[('Christchurch', 'Gold Coast'),
               ('Christchurch','Auckland'),
               ('Christchurch','Wellington'),
               ('Wellington', 'Gold Coast'),
               ('Wellington', 'Auckland'),
               ('Auckland', 'Gold Coast')],
    starting_nodes=['Christchurch'],
    goal_nodes={'Gold Coast'})

my_itinerary = next(generic_search(available_flights, DFSFrontier()), None)
print_actions(my_itinerary)

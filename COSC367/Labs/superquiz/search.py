"""This module contains classes and functions related to graph
search. It is specifically written for the course COSC367: Artificial
Intelligence. Most of the code here is abstract.  The normal usage is
to write concrete subclasses for particular problems.

Author: Kourosh Neshatian
Last modified: 13 Jul 2019

"""

from abc import ABCMeta, abstractmethod
from collections import namedtuple

def generic_search(graph, frontier):
    """Implements a generic graph search algorithm (see the lecture
    notes). The actual search behaviour depends on the type of the
    frontier object.

    """

    for starting_node in graph.starting_nodes():
        # Paths are tuples and the first arc on each path is a dummy
        # arc to a starting node
        frontier.add((Arc(None, starting_node, "no action", 0),))

    for path in frontier:
        node_to_expand = path[-1].head # head of the last arc in the path

        if graph.is_goal(node_to_expand):
            yield path

        for arc in graph.outgoing_arcs(node_to_expand):
            frontier.add(path + (arc,)) # add back a new extended path


class Arc(namedtuple('Arc', 'tail, head, action, cost')):
    """Represents an arc in a graph.

    Keyword arguments:
    tail -- the source node (state)
    head -- the target node (state)
    action -- a string describing the action that must be taken in
             order to get from the source state to the destination state.
    cost -- a number that specifies the cost of the action
    """


class Graph(metaclass=ABCMeta):
    """This is an abstract class for graphs. It cannot be directly
    instantiated. You should define a subclass of this class
    (representing a particular problem) and implement the expected
    methods."""

    @abstractmethod
    def is_goal(self, node):
        """Returns true if the given node is a goal state, false otherwise."""

    @abstractmethod
    def starting_nodes(self):
        """Returns a sequence of starting nodes. Often there is only one
        starting node but even then the function returns a sequence
        with one element. It can be implemented as an iterator if
        needed.

        """

    @abstractmethod
    def outgoing_arcs(self, tail_node):
        """Given a node it returns a sequence of arcs (Arc objects)
        which correspond to the actions that can be taken in that
        state (node)."""

    def estimated_cost_to_goal(self, node):
        """Return the estimated cost to a goal node from the given
        state. This function is usually implemented when there is a
        single goal state. The function is used as a heuristic in
        search. The implementation should make sure that the heuristic
        meets the required criteria for heuristics."""

        raise NotImplementedError


class ExplicitGraph(Graph):
    """This is a concrete subclass of Graph where vertices and edges
     are explicitly enumerated. Objects of this type are useful for
     testing graph algorithms."""

    def __init__(self, nodes, edge_list, starting_nodes, goal_nodes, estimates=None):
        """Initialises an explicit graph.
        Keyword arguments:
        nodes -- a set of nodes
        edge_list -- a sequence of tuples in the form (tail, head) or
                     (tail, head, cost)
        starting_nodes -- the list of starting nodes. We use a list
                          to remind you that the order can influence
                          the search behaviour.
        goal_node -- the set of goal nodes. It's better if you use a set
                     here to remind yourself that the order does not matter
                     here. This is used only by the is_goal method.
        """

        # A few assertions to detect possible errors in
        # instantiation. These assertions are not essential to the
        # class functionality.
        assert all(tail in nodes and head in nodes for tail, head, *_ in edge_list)\
           , "An edge must link two existing nodes!"
        assert all(node in nodes for node in starting_nodes),\
            "The starting_states must be in nodes."
        assert all(node in nodes for node in goal_nodes),\
            "The goal states must be in nodes."

        self.nodes = nodes
        self.edge_list = edge_list
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes
        self.estimates = estimates

    def starting_nodes(self):
        """Returns a sequence of starting nodes."""
        return self._starting_nodes

    def is_goal(self, node):
        """Returns true if the given node is a goal node."""
        return node in self.goal_nodes

    def outgoing_arcs(self, node):
        """Returns a sequence of Arc objects that go out from the given
        node. The action string is automatically generated.

        """
        arcs = []
        for edge in self.edge_list:
            if len(edge) == 2:  # if no cost is specified
                tail, head = edge
                cost = 1        # assume unit cost
            else:
                tail, head, cost = edge
            if tail == node:
                arcs.append(Arc(tail, head, str(tail) + '->' + str(head), cost))
        return arcs



class Frontier(metaclass = ABCMeta):
    """This is an abstract class for frontier classes. It outlines the
    methods that must be implemented by a concrete subclass. Concrete
    subclasses determine the search strategy.

    """


    @abstractmethod
    def add(self, path):
        """Adds a new path to the frontier. A path is a sequence (tuple) of
        Arc objects. You should override this method.

        """


    def __iter__(self):
        """We don't need a separate iterator object. Just return self. You
        don't need to change this method."""
        return self


    @abstractmethod
    def __next__(self):

        """Selects, removes, and returns a path on the frontier if there is
        any.Recall that a path is a sequence (tuple) of Arc
        objects. Override this method to achieve a desired search
        strategy. If there nothing to return this should raise a
        StopIteration exception.

        """



def print_actions(path):
    """Given a path (a sequence of Arc objects), prints the actions that
    need to be taken and the total cost of those actions. The path is
    usually a solution (a path from the starting node to a goal
    node."""

    if path:
        print("Actions:")
        print(",\n".join("  {}".format(arc.action) for arc in path[1:]) + ".")
        print("Total cost:", sum(arc.cost for arc in path))
    else:
        print("There is no solution!")


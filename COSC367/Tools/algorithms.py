from search import *
from csp import *
import heapq, re
import math, itertools, copy

""" Constants """

BLANK = ' '

""" Frontiers """

class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self, trace=False):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []
        self.trace = trace

    def add(self, path):
        if self.trace: print(f"+ {trace(path)}")
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            tmp = self.container.pop()
            if self.trace: print(f"- {trace(tmp)}")
            return tmp
        else:
            raise StopIteration

class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self, trace=False):
        """The constructor takes no argument. It initialises the
        container to an empty queue."""
        self.container = Queue()
        self.trace = trace

    def add(self, path):
        if self.trace: print(f"+ {trace(path)}")
        self.container.enqueue(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            tmp = self.container.dequeue()
            if self.trace: print(f"- {trace(tmp)}")
            return tmp
        else:
            raise StopIteration

class LCFSFrontier(Frontier):
    """Implements an LCFS frontier container"""

    def __init__(self, trace=False):
        """The constructor takes no argument. It initialises the
        container to an empty heap."""
        self.heap = []
        self.trace = trace
        self.popped = []

    def add(self, path):
        total_cost = 0
        for arc in path:
            total_cost += arc.cost
        if self.trace: print(f"+ {trace(path, check=True)}")
        heapq.heappush(self.heap, (total_cost, path))

    def __next__(self):
        if len(self.heap) > 0:
            tmp = heapq.heappop(self.heap)[1]
            if self.trace and self._prune_path(tmp[-1]): self.popped.append(f"- {trace(tmp, check=True)}"); print(f"- {trace(tmp, check=True)}! \t this is with pruning (ignore all expanded nodes from this path when pruned)")
            elif self.trace: self.popped.append(f"- {trace(tmp, check=True)}"); print(f"- {trace(tmp, check=True)}")
            return tmp
        else:
            raise StopIteration

    def _prune_path(self, arc):
        """Checks if the arc is in the heap"""
        for path in self.popped:
            if path[0] == "-":
                tmp = "".join(c for c in path if c.isalpha())
                if tmp[-1] == arc[1]:
                    return True
        return False

class AStarFrontier(Frontier):
    def __init__(self, map_graph, trace=False):
        self.map_graph = map_graph
        self.container = []
        self.visited = set()
        self.counter = 0
        self.trace = trace

    def add(self, path):
        if path[-1].head not in self.visited:
            cost = 0
            for arc in path:
                cost += arc.cost
            cost += self.map_graph.estimates[str(path[-1].head)]
            if self.trace: print(f"+ {trace(path)}")
            heapq.heappush(self.container, (cost, self.counter, path))
            self.counter += 1

    def __next__(self):
        while self.container:
            candidate = heapq.heappop(self.container)[2]
            head = candidate[-1].head
            if head not in self.visited:
                if self.trace: print(f"- {trace(candidate)}")
                self.visited.add(head)
                return candidate
        raise StopIteration

""" Perceptrons """

def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""

    def perceptron(input):
        # Complete (a line or two)
        sum = bias
        for i in range(len(weights)):
            sum += weights[i] * input[i]
        # Note: we are masking the built-in input function but that is
        # fine since this only happens in the scope of this function and the
        # built-in input is not needed here.
        return 1 if sum >= 0 else 0

    return perceptron  # this line is fine

def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    n = len(weights)
    for _ in range(max_epochs):
        for i, ex in enumerate(training_examples):
            a = bias
            for j in range(n):
                a += ex[0][j] * weights[j]
            g = 1 if a >= 0 else 0
            print("Perceptron output: {}, Expected output: {}".format(g, ex[1]))
            if g != ex[1]:
                for j in range(n):
                    weights[j] = weights[j] + learning_rate * ex[0][j] * (ex[1] - g)
                bias = bias + learning_rate * (ex[1] - g)
            print("Weights: {}. Bias: {}".format(weights, bias))
    return (weights, bias)

""" Graphs """

class RoutingGraph(Graph):
    def __init__(self, map_str):
        self.map_str = map_str
        self.map_graph = []
        self.start_nodes = []
        self.goal_nodes = []
        self.directions = {
            'N':  (-1, 0),
            'E':  (0, 1),
            'S':  (1, 0),
            'W':  (0, -1),
        }

        self.process_map(self.map_str)

    def process_map(self, map_str):
        map_matrix = (map_str.strip()).split('\n')
        for j in map_matrix:
            self.map_graph.append(list(j.strip()))
        for j in range(len(self.map_graph)):
            for k in range(len(self.map_graph[j])):
                if self.map_graph[j][k] == 'S':
                    self.start_nodes.append((j, k, math.inf))
                elif self.map_graph[j][k].isdigit():
                    self.start_nodes.append((j, k, int(self.map_graph[j][k])))
                elif self.map_graph[j][k] == 'G':
                    self.goal_nodes.append((j, k))

    def starting_nodes(self):
        for starting_node in self.start_nodes:
            yield starting_node

    def is_goal(self, node):
        return (node[0], node[1]) in self.goal_nodes

    def outgoing_arcs(self, tail):
        for direction in self.directions.items():
            walls = "X+-|"
            direct_y = tail[0] + direction[1][0]
            direct_x = tail[1] + direction[1][1]
            if self.map_graph[direct_y][direct_x] not in walls and tail[2] > 0:
                head = (direct_y, direct_x, tail[2] - 1)
                yield Arc(tail, head, direction[0], 5)
        if self.map_graph[tail[0]][tail[1]] == 'F' and tail[2] < 9:
            head = (tail[0], tail[1], 9)
            yield Arc(tail, head, 'Fuel up', 15)

    def estimated_cost_to_goal(self, node):
        lowest = math.inf
        for goal in self.goal_nodes:
            dist = 5 * (abs(goal[0]-node[0]) + abs(goal[1]-node[1]))
            if dist < lowest:
                lowest = dist
        return lowest

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

class OrderedExplicitGraph(ExplicitGraph):
    def __init__(self, nodes, edges, starting_list, goal_nodes):
        self.nodes = nodes
        self.edges = edges
        self.starting_list = starting_list
        self.goal_nodes = goal_nodes

        self.edges = list(self.edges)
        self.edges = sorted(self.edges, key=lambda edge: (edge[0], edge[1]), reverse=True)

    def outgoing_arcs(self, node):
        """Returns a sequence of Arc objects corresponding to all the
        edges in which the given node is the tail node. The label is
        automatically generated."""

        for edge in self.edges:

            if len(edge) == 2:  # if no cost is specified
                tail, head = edge
                cost = 1  # assume unit cost
            else:
                tail, head, cost = edge
            if tail == node:
                yield Arc(tail, head, str(tail) + '->' + str(head), cost)

class KBGraph(ExplicitGraph):
    """return a standard from of graph with variables nodes, edge list, starting nodes, goal nodes"""

    def __init__(self, kb, query):
        """
        initialses an KBGraph.
        Keyword arguments:
        kb -- a set of knowledge bases from class clauses,
        query -- a set of atoms whether derived or not.
        """

        self.kb = list(clauses(kb))
        self.query = query

        nodes = []
        edge_list = []
        starting_list = []

        for clause in self.kb:

            if clause[0] not in nodes:
                nodes.append(clause[0])

            if clause[1] == []:
                starting_list.append(clause[0])

            for atom in clause[1]:
                if atom not in nodes:
                    nodes.append(atom)

                edge_list.append((atom, clause[0]))

        for goal in self.query:
            if goal not in nodes:
                nodes.append(goal)

        ExplicitGraph.__init__(self, nodes, edge_list, starting_list, goal_nodes = self.query, estimates=None)

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

""" Tools needed """
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

def trace(path, check=False):
        trace = ""
        cost = 0
        for arc in path:
            trace += str(arc[1])
        for arc in path:
            cost += arc[3]
        return trace + ", " + str(cost) if check else trace

def print_map(map_graph: RoutingGraph, frontier: AStarFrontier, solution):
    map = map_graph.map_graph
    for path in frontier.visited:
        if map[path[0]][path[1]] not in "SG*":
            map[path[0]][path[1]] = "."
    if solution:
        for path in solution:
            if map[path.head[0]][path.head[1]] not in "SG":
                map[path.head[0]][path.head[1]] = "*"
    out = ""
    for i in map:
        for j in i:
            out += j
        out += "\n"
    print(out)
    return out

def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    to_do = {(x, c) for c in csp.constraints for x in scope(c)} # COMPLETE
    while to_do:
        x, c = to_do.pop()
        ys = scope(c) - {x}
        new_domain = set()
        for xval in csp.var_domains[x]: # COMPLETE
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c):
                    new_domain.add(xval) # COMPLETE
                    break
        if csp.var_domains[x] != new_domain:
            for cprime in set(csp.constraints) - {c}:
                if x in scope(cprime):
                    for z in scope(cprime): # COMPLETE
                        if x != z: # COMPLETE
                            to_do.add((z, cprime))
            csp.var_domains[x] = new_domain     #COMPLETE
    return csp

def forward_deduce(knowledge_base):
    derived_atoms = []
    Clauses = list(clauses(knowledge_base))
    counter = 0
    while counter < len(Clauses):
        for clause in Clauses:
            if not clause[1] or set(clause[1]).issubset(set(derived_atoms)):
                derived_atoms.append(clause[0])
                Clauses.remove(clause)
                counter = 0
            else:
                counter += 1

    return set(derived_atoms)

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- kourosh neshatian
    """
    ATOM   = r"[a-z][a-zA-z\d_]*"
    HEAD   = r"\s*(?P<HEAD>{ATOM})\s*".format(**locals())
    BODY   = r"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*".format(**locals())
    CLAUSE = r"{HEAD}(:-{BODY})?\.".format(**locals())
    KB     = r"^({CLAUSE})*\s*$".format(**locals())

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")

def learn_perceptron(weights, bias, training_examples, learning_rate,
                     max_epochs):
    for epoch in range(1, max_epochs + 1):
        seen_error = False
        for input, target in training_examples:
            a = bias + sum(weights[i] * input[i] for i in range(len(input)))
            output = 1 if a >= 0 else 0
            if output != target:
                seen_error = True
                weights = [weights[i] + learning_rate * input[i] * (target - output) for i in range(len(input))]
                bias = bias + learning_rate * (target - output)
        if not seen_error:
            def perceptron(input_vector):
                a = bias + sum(weights[i] * input_vector[i] for i in range(len(input)))
                output = 1 if a >= 0 else 0
                return output
            return perceptron

""" Minimax """
max_val = lambda tree: tree if type(tree) is int \
    else max([min_val(tree[i]) for i in range(len(tree))])
min_val = lambda tree: tree if type(tree) is int \
    else min([max_val(tree[i]) for i in range(len(tree))])

def min_action_value(tree):
    index = 0
    high = float("inf")
    if type(tree) is int:
        return (None, tree)
    for i in range(len(tree)):
        tmp = max_val(tree[i])
        if tmp < high:
            high = tmp
            index = i
    return (index, high)

def max_action_value(tree):
    index = 0
    low = float("-inf")
    if type(tree) is int:
        return (None, tree)
    for i in range(len(tree)):
        tmp = min_val(tree[i])
        if tmp > low:
            low = tmp
            index = i
    return (index, low)

if __name__ == "__main__":

    """ Tracing graphs using frontiers """

    g = ExplicitGraph(
        nodes={'A', 'B', 'C', 'G'},
        edge_list=[('A', 'B'), ('A', 'G'), ('B', 'C'), ('C', 'A'), ('C', 'G')],
        starting_nodes=['A', 'B'],
        goal_nodes={'G'},
    )

    print()
    print("-------------- Trace -------------")
    print()
    solutions = generic_search(g, DFSFrontier(trace=True))
    solution = next(solutions, None)
    print()
    print("------------- Result ------------")
    print()
    print_actions(solution)
    print()
    print("---------------------------------")

    """ Tracing perceptrons """
    # weights = [-0.5, 0.5]
    # bias = -0.5
    # learning_rate = 0.5

    # examples = [
    #     ([1, 1],   0),    # index 0 (first example)
    #     ([2, 0],   1),
    #     ([1, -1],  0),
    #     ([-1, -1], 1),
    #     ([-2, 0],  0),
    #     ([-1, 1],  1),
    # ]
    # max_epochs = 1

    # weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
    # print(f"Weights: {weights}")
    # print(f"Bias: {bias}\n")
    # perceptron = construct_perceptron(weights, bias)

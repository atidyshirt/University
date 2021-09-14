import math
from search import Graph, Arc

def get_key(val, dic):
    for key, value in dic.items():
         if val == value:
             return key
    return None

class RoutingGraph(Graph):
    def __init__(self, map_str):
        self.map_str = map_str
        self.map_graph = []
        self.start_nodes = []
        self.goal_nodes = []
        self.directions = {
            'N':  (-1, 0),
            'E' :  (0, 1),
            'S' :  (1, 0),
            'W' :  (0, -1),
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


if __name__ == '__main__':
    map_str = """\
    +-------+
    |  9  XG|
    |X XXX  |
    | S  0FG|
    +-------+
    """

    graph = RoutingGraph(map_str)

    print("Starting nodes:", sorted(graph.starting_nodes()))
    print("Outgoing arcs (available actions) at starting states:")
    for s in sorted(graph.starting_nodes()):
        print(s)
        for arc in graph.outgoing_arcs(s):
            print ("  " + str(arc))

    node = (1,1,5)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))

    node = (1,7,2)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))

    node = (3, 7, 0)
    print("\nIs {} goal?".format(node), graph.is_goal(node))

    node = (3, 7, math.inf)
    print("\nIs {} goal?".format(node), graph.is_goal(node))

    node = (3,6,5)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))

    node = (3,6,9)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))

import math
import heapq
from search import *
from markdown_writer.markdown_writer import MarkdownWriter

INF = math.inf

class AStarFrontier(Frontier):
    def __init__(self, map_graph):
        self.map_graph = map_graph
        self.container = []
        self.visited = set()
        self.counter = 0

    def add(self, path):
        if path[-1].head not in self.visited:
            cost = 0
            for arc in path:
                cost += arc.cost
            cost += self.map_graph.estimated_cost_to_goal(path[-1].head)
            heapq.heappush(self.container, (cost, self.counter, path))
            self.counter += 1

    def __next__(self):
        while self.container:
            candidate = heapq.heappop(self.container)[2]
            head = candidate[-1].head
            if head not in self.visited:
                self.visited.add(head)
                return candidate
        raise StopIteration


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
        lowest = INF
        for goal in self.goal_nodes:
            dist = 5 * (abs(goal[0]-node[0]) + abs(goal[1]-node[1]))
            if dist < lowest:
                lowest = dist
        return lowest


def get_key(val, dic):
    for key, value in dic.items():
        if val == value:
            return key
    return None

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

def report(graph, frontier, solution):
    md = MarkdownWriter("./report.md")
    md.header1("Map Algorithm Data")
    md.paragraph("""Here is an example of the A\*
    algorithm traversing a map string, the agent
    can pick up fuel, traverse the space until it reaches
    a goal node, note the border and X characters are
    considered walls and cannot be moved through,
    `.` identifies places popped and `*` identifies the
    selected path.
    """)
    md.codeblock(graph.map_str)
    md.paragraph("""The output (traversed graph) is as follows:""")
    md.codeblock(print_map(graph, frontier, solution))


if __name__ == "__main__":
    map_str = """\
    +------------+
    |         X  |
    | S    XXXX G|
    |   X  X     |
    |   X     X  |
    |   X  X  X X|
    +------------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)
    report(map_graph, frontier, solution)

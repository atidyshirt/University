class Vec:
    """A simple vector in 2D. Also used as a position vector for points"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, scale):
        return Vec(self.x * scale, self.y * scale)
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y
        
    def lensq(self):
        return self.dot(self)

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)


""" FUNCTIONS FOR VEC CLASS """
def signed_area(a, b, c):
    """ FUNCTION TO RETURN SIGNED AREA (AREA OF TRIANGE * 2) """
    p = b - a
    q = c - a
    return (p.x * q.y - q.x * p.y)

""" FUNCTIONS TO CHECK IF TRIANGLE IS ROTATING COUNTER CLOCKWISE """
def is_ccw(p, b, c):
    """ implementation with signed area function """
    return signed_area(p, b, c) > 0

def is_ccw_(a, b, c):
    """ independent implementation (without signed_area) """
    p = b - a
    q = c - a
    if (p.x * q.y - q.x * p.y) > 0:
        boo = True
    else:
        boo = False
    return boo

def turn(a, b, c):
    """ independent implementation (without signed_area) """
    p = b - a
    q = c - a
    return p.x * q.y - q.x * p.y


def leftmost_vertex(polygon, p):
    leftmost = polygon[0]
    current = 0
    for x in range(len(polygon)):
        print(turn(p, polygon[x], leftmost))
        if turn(p, leftmost, polygon[x]) > current:
            leftmost = polygon[x]
            current = turn(p, polygon[x], leftmost)
    return leftmost

def intersecting(a, b, c, d):
    if is_ccw(a, d, b) != is_ccw(a, c, b):
        if is_ccw(c, a, d) != is_ccw(c, b, d):
            boo = True
        else: boo = False
    else:
        boo = False
    return boo

def is_on_segemnt(p, a, b):
    if b > a:
        line = b - a
    elif a > b:
        line = a - b
    else:
        line = a


def convex_hull_naive(S):
    """ check if an edge is in hull, compare it to each other edges to ensure
        that nothing is beyond that point, this is a really bad meothod O(n^3)
    """
    hull = []
    for p in S:
        for q in S:
            if q != P:
                edge_in_hull = True
                for r in S:
                    if r != q or r != p:
                        if not is_ccw(p, q, r):
                            edge_in_hull = False
            if edge_in_hull:
                hull.append((p, q))

def gift_wrap(S):
    """ Gift wrap solution to generating a convex hull around a set of points
        works by finding the bottom most and then finding the right most points
        ect until it forms a perimeter around all vertexes
    """
    lowest = float('inf')
    for vertex in S:
        if vertex.y < lowest:
            lowest = vertex.y
            bottommost = vertex
        
    hull = [bottommost]

    closed = False

    counter = 0
    while hull is not closed:
        candidate = None

        for p in S:
            counter += 1
            if candidate is None or is_ccw(hull[counter-1], p, candidate):
                candidate = p
        hull.append(candidate)

    return hull


""" TESTS """
square = [Vec(0, 0), Vec(100, 0), Vec(100, 100), Vec(0, 100)]
p = Vec(-50, 50)
leftmost = leftmost_vertex(square, p)
print(leftmost)

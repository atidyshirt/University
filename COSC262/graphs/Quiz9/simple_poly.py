from functools import cmp_to_key  # Converts a cmp function to a key function

class PointSortKey:
    """A class for use as a key when sorting points wrt anchor point"""
    def __init__(self, p, anchor):
        self.vec = p - anchor       # Direction vector from anchor to p
        self.is_anchor = self.vec.lensq() == 0 # True iff p == anchor
   
    def __lt__(self, other):
        """Compares two sort keys. p1 < p2 means the vector from the
           anchor point to p2 is to the left of the vector from the
           anchor to p1.
        """
        if self.is_anchor:
            return True   # Ensure anchor point < all other points
        elif other.is_anchor:
            return False  # Ensure no other point < the anchor
        else:
            area = self.vec.x * other.vec.y - other.vec.x * self.vec.y
            return area > 0  #area > 0 => is_ccw => p1 < p2


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

def simple_polygon(points):
    def sort_key(v):
        return v.y
    points_sorted = [sort_key(v) for v in points]
    x = float('inf')
    index_of_smallest = -1
    for i in len(points_sorted):
        if points_sorted[i] < x:
            x = points_sorted[i]
            index_of_smallest = i
    anchor = points[i]

    def cmp(p1, p2):
        """ Compares two points with respect to a globally defined anchor point.
            Returns a negative, zero or positive value according to whether p1 is
            to the right of p2 ("p1 < p2"), collinear with it ("p1 == p2") or to
            the left ("p1 > p2").
         """
        v1 = p1 - anchor
        v2 = p2 - anchor
        if v1.lensq() == 0:   # Is p1 the anchor point (or a copy of it)?
            return -1         # Yes. Make sure anchor point < everything else
        elif v2.lensq() == 0: # Is p2 the anchor point (or a copy of it)?
            return +1         # Yes, Make sure all other points > anchor
        else:  # In all other cases, return the negative of the usual area
            return v2.x * v1.y - v1.x * v2.y  # This is negative if p1 < p2

        simply_poly = sorted(points, key=cmp_to_key(cmp))
        return simply_poly

points = [
    Vec(100, 100),
    Vec(0, 100),
    Vec(50, 0)]
verts = simple_polygon(points)
print(verts)
for v in verts:
    print(v)
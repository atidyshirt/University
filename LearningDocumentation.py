class Vector2d:
    """A 2D vector object

    Object that contains values representing
    placement on the x and y axis. Format: (x, y).

    Attributes
    ----------
    x : int
        an integer representing the x axis position.
    y : int
        an integer representing the y axis position.

    Returns
    -------
    (x, y) : Vector2d
    """
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    # Here is a comment

    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2d(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2d(self.x * other.x, self.y * other.y)

    def cube(self):
        """ Cubes a 2D Vector """
        return Vector2d(self.x**3, self.y**3)

    def __repr__(self):
        return f"({self.x}, {self.y})"

def adding_vectors(lov: list[Vector2d]):
    final = Vector2d()
    for vector in lov:
        final += vector
    return final

set1 = {"this", "is", "an", "array", "of", "vectors"}

list_of_vectors = [Vector2d(5, 4), Vector2d(3, 2), Vector2d(5, 2)]

vec1 = Vector2d(1, 3)

vec2 = Vector2d(3, 4)

print(vec1 + vec2)
print(vec1 * vec2)
print(Vector2d.cube(vec1 + vec2))
print(adding_vectors(list_of_vectors))

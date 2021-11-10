from csp import *

csp = CSP(
    var_domains = {var:{1,2,3,4} for var in 'abc'},
    constraints = {
        lambda a, b, c: a < b < c,
        lambda b: b % 2 == 0,
    }
)

relations = [
    Relation(
        header = ['a', 'b','c'],
        tuples = {
            (1, 2, 3),
            (1, 3, 4),
            (2, 3, 4),
            (1, 2, 4),
        }
    ),
    Relation(
        header = ['b'],
        tuples = {
            (2,),
            (4,),
        }
    ),
]

relations_after_elimination = [
    Relation(
        header = ['a', 'c'],
        tuples = {
            (1,2),
            (1,3),
            (1,4),
            (2,3),
            (2,4),
            (3,4),
        }
    ),
]

from csp import CSP, Relation

csp = CSP(
    var_domains = {var:{-1,0,1} for var in 'abc'},
    constraints = {
        lambda a, b: a * b == -1,
        lambda b, c: b + c == 1,
    }
)


relations = [
    Relation(
        header = ['a', 'b'],
        tuples = [
            (-1, 1),
            (1, -1)
        ]),
    Relation(
        header = ['b', 'c'],
        tuples = [
            (1, 0),
            (0, 1)
        ])
]

relations_after_elimination = [
    Relation(
        header = ['a', 'c'],
        tuples = [(-1, 0)]
    ),
]

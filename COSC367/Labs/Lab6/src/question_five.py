from csp import Relation


relations = [
    Relation(header=['a', 'b', 'c'],
        tuples={
            (1, 0, 0),
            (2, 0, 0),
            (2, 0, 1),
            (2, 1, 0)
        }
    ),
    Relation(header=['c', 'd'],
        tuples={
            (1, 0),
            (2, 0),
            (2, 1)
        }
    )
]

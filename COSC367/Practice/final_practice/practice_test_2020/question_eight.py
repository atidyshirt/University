from csp import Relation, CSP

csp = CSP(
    var_domains = {var:{-1,0,1} for var in 'abc'},
    constraints = {
        lambda a, b: a * b > 0,
        lambda b, c: b + c > 0,
    }
)

relations = [
    Relation(
        header = ["a", "b"],
        tuples = {
            (-1, -1),
            (1, 1)
        }
    ),
    Relation(
        header = ["b", "c"],
        tuples = {
            (0, 1),
            (0, 1)
        }
    ),
]

relations_after_elimination = [

]

print(type(relations) is list)
print(all(type(r) is Relation for r in relations))
print()
print(type(relations_after_elimination) is list)
print(all(type(r) is Relation for r in relations_after_elimination))

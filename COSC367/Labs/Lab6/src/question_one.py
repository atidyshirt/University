from csp import *
import itertools

def generate_and_test(csp):
    assignments = []
    for value in itertools.product(*csp.var_domains.values()):
        assignments.append(dict(zip(csp.var_domains.keys(), value)))
    for a in assignments:
        broken_constraint = False
        for c in csp.constraints:
            if not satisfies(a, c):
                broken_constraint = True
                break
        if not broken_constraint:
            yield a


if __name__ == '__main__':
    simple_csp = CSP(
        var_domains={x: set(range(1, 5)) for x in 'abc'},
        constraints={
            lambda a, b: a < b,
            lambda b, c: b < c,
            })

    solutions = sorted(str(sorted(solution.items())) for solution
                       in generate_and_test(simple_csp))
    print("\n".join(solutions))

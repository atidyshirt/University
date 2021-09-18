from csp import *
import itertools, copy


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


def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    to_do = {(x, c) for c in csp.constraints for x in scope(c)} # COMPLETE
    while to_do:
        x, c = to_do.pop()
        ys = scope(c) - {x}
        new_domain = set()
        for xval in csp.var_domains[x]: # COMPLETE
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c):
                    new_domain.add(xval) # COMPLETE
                    break
        if csp.var_domains[x] != new_domain:
            for cprime in set(csp.constraints) - {c}:
                if x in scope(cprime):
                    for z in scope(cprime): # COMPLETE
                        if x != z: # COMPLETE
                            to_do.add((z, cprime))
            csp.var_domains[x] = new_domain     #COMPLETE
    return csp


cryptic_puzzle = CSP(
    var_domains={x: set(range(0, 10)) for x in 'twofur'},
    constraints={
        lambda t, w, o, f, u, r: len([t, w, o, f, u, r]) == len(set([t, w, o, f, u, r])),
        lambda o, r: (o + o) % 10 == r,
        lambda t, o, w: (t + t + ((w + w) // 10)) % 10 == o,
        lambda w, u, o: (w + w + ((o + o) // 10)) % 10 == u,
        lambda f: f == 1,
        lambda t: t >= 5,
    }
)

print(set("twofur") <= set(cryptic_puzzle.var_domains.keys()))
print(all(len(cryptic_puzzle.var_domains[var]) == 10 for var in "twour"))
